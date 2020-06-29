#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
import pandas as pd
import uproot

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--proc", type=str, help="ggH, VBFH, WminusH, WplusH, ZH, ttH", default='ggH', required=False)

args = parser.parse_args()
process = args.proc

url = 'https://gist.githubusercontent.com/bonanomi/d14780f7562cb2a22fdd753a9d4459d4/raw/b3c6d77505b90eb38a886c19a31725df8ceb908f/MyMPLStyle'
plt.style.use(url)

tree = 'Events'
path = '/eos/user/m/mbonanom/HIGSTXS/stxs_trees/'
name = 'nanoAOD_%s_HZZ4L.root' %process
fname = path + name

if (process == 'ggH') | (process == 'ttH'):
    branches = ['HTXS_stage1_2_cat_pTjet30GeV', 'LHEScaleWeight']
else:
    branches = ['HTXS_stage1_1_cat_pTjet30GeV', 'LHEScaleWeight']

evt = uproot.open(fname)[tree]
evts = evt.arrays(branches)

binning = np.linspace(0, 900, 900)

if (process == 'ggH') | (process == 'ttH'):
    stxs_cat = evts[b'HTXS_stage1_2_cat_pTjet30GeV']
else:
    stxs_cat = evts[b'HTXS_stage1_1_cat_pTjet30GeV']

h_stxs = np.histogram(stxs_cat, binning)


d = {}
for i in range(9):
    d[i] = [j[i] for j in evts[b'LHEScaleWeight']]


d_scales = {}
for i in range(9):
    d_scales[i] = np.histogram(stxs_cat, binning, weights=d[i])


int_nominal = [i for i in h_stxs[0] if i!=0]

int_scale = {}
for i in range(9):
    if (i==2) | (i==6):
        continue
    int_scale[i] = [j for j, k in zip(d_scales[i][0], h_stxs[0]) if k != 0]


bins_c =  0.5*(h_stxs[1][1:]+h_stxs[1][:-1])

stxs_bins = [round(j, 0) for i, j in zip(h_stxs[0], bins_c) if i!=0]

for stxs, nom_int in zip(enumerate(stxs_bins), int_nominal):
    k = stxs[0]; stxs_bin = stxs[1]
    print('[{}] => {} :::'.format(int(stxs_bin), nom_int), end='')
    for i in range(9):
        if (i==2) | (i==6):
            continue
        print(' {0:.2f}, '.format(int_scale[i][k]), end='')
    print('\n')
print('\n\n')

for stxs, nom_int in zip(enumerate(stxs_bins), int_nominal):
    k = stxs[0]; stxs_bin = stxs[1]
    print('[{}] => {} :::'.format(int(stxs_bin), nom_int), end='')
    for i in range(9):
        if (i==2) | (i==6):
            continue
        norm_stxs = (int_scale[i][k] - nom_int)/nom_int * 1e2
        print(' {0:.2f}%, '.format(norm_stxs), end='')
    print('\n')
print('\n\n')

for stxs, nom_int in zip(enumerate(stxs_bins), int_nominal):
    k = stxs[0]; stxs_bin = stxs[1]
    print('[{}] => :::'.format(int(stxs_bin)), end='')
    for i in range(9):
        if (i==2) | (i==6):
            continue
        norm_stxs = nom_int/(int_scale[i][k])
        print(' {0:.4f}, '.format(norm_stxs), end='')
    print('\n')
print('\n\n')

integrals = {i: {int(k): [] for k in stxs_bins} for i in range(9) if ((i!= 2) & (i!= 6))}
for stxs, nom_int in zip(enumerate(stxs_bins), int_nominal):
    k = stxs[0]; stxs_bin = int(stxs[1])
    for i in range(9):
        if (i==2) | (i==6):
            continue
        int_varied = int_scale[i][k]
        integrals[i][stxs_bin] = (int_varied)

yields = open("Yields_1p2_%s.txt" %process,"w+")
yields.write('STXS\t\t DD \t\t DN \t\t ND \t\t NN \t\t NU \t\t UN \t\t UU')
yields.write('\n')

for stxs, nom_int in zip(enumerate(stxs_bins), int_nominal):
    k = stxs[0]; stxs_bin = int(stxs[1])
    yields.write('{} \t'.format(int(stxs_bin)))
    for i in range(9):
        if (i==2) | (i==6):
            continue
        yields.write('\t{0:.2f},\t ' .format(integrals[i][stxs_bin]))
    yields.write('\n')
yields.close()


normalization = open("Normalization_1p2_%s.txt" %process,"w+")
normalization.write('STXS\t\t DD \t\t DN \t\t ND \t\t NN \t\t NU \t\t UN \t\t UU')
normalization.write('\n')
for stxs, nom_int in zip(enumerate(stxs_bins), int_nominal):
    k = stxs[0]; stxs_bin = int(stxs[1])
    normalization.write('{} \t'.format(int(stxs_bin)))
    print(stxs_bin, end = "\t")
    for i in range(9):
        if (i==2) | (i==6):
            continue
        norm_int = nom_int/integrals[i][stxs_bin]
        normalization.write('\t{0:.2f},\t ' .format(norm_int))
        if (i == 0) | (i == 8):
            print(norm_int, end = "\t")
    print("\n")
    normalization.write('\n')
normalization.close()

histos = {}
for i in range(9):
    if (i==2) | (i==6):
        continue    
    values = []
    for stxs, nom_int in zip(enumerate(stxs_bins), int_nominal):
        k = stxs[0]; stxs_bin = int(stxs[1])
        norm_int = nom_int/integrals[i][stxs_bin]
        values.append(norm_int)
    histos[i] = values


scale_var = {
    0: r'$\mu_r$ = 0.5, $\mu_f$ = 0.5',
    1: r'$\mu_r$ = 0.5, $\mu_f$ = 1.0',
    3: r'$\mu_r$ = 1.0, $\mu_f$ = 0.5',
    4: r'$\mu_r$ = 1.0, $\mu_f$ = 1.0',
    5: r'$\mu_r$ = 1.0, $\mu_f$ = 2.0',
    7: r'$\mu_r$ = 2.0, $\mu_f$ = 1.0',
    8: r'$\mu_r$ = 2.0, $\mu_f$ = 2.0'
}

s_bin = [int(s) for s in stxs_bins]
xvals = range(len(stxs_bins))

plt.figure(figsize = (6,5))
cmap = plt.cm.coolwarm(np.linspace(0, 1., 9.))
for i in range(9):
    if (i==2) | (i==6):
        continue
    plt.step(xvals, histos[i], where = 'mid', label = scale_var[i], color = cmap[i], linewidth = 1.5)
    plt.grid(b = None)

plt.xticks(xvals, s_bin, rotation = 45)
plt.tick_params(which='minor', length=0)
plt.tick_params(axis='x', which='major', top = False, length=6)
plt.tick_params(axis='x', which='minor', top = False, length=3)
plt.tick_params(axis='y', which='major', right = False, length=6)
plt.tick_params(axis='y', which='minor', right = False, length=3)
plt.legend(bbox_to_anchor=(1., 0.9))
plt.tick_params(which='minor', length=0)
if process == 'VBFH':
    plt.ylim(0.9, 1.1)
else:
    plt.ylim(0.5, 1.5)
plt.title('STXS 1.2 bins uncertainties')
plt.xlabel('STXS 1.2 Bin', ha='right', x=1.0, fontsize = 12)
plt.ylabel(r'$\sigma_{nom}/\sigma_{var}$', ha='right', y=1.0, fontsize = 12)
plt.show()
plt.savefig('STXS1p2_Unc_%s.pdf' %process, bbox_inches='tight')
