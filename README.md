# STXS_Unc
Sample notebooks to compute STXS bins uncertainties for both Stages 1.1 and 1.2.
The uncertainties are computed following the scheme presented [here](https://cernbox.cern.ch/index.php/s/lq8XUoJ4WjDCPlL).
In each STXS bin the inclusive yield is computed, as well as the yield corresponding to mutual variations of the renormalization and factorization scales (mu_R and mu_F respectively). 

## STXS 1.1
The bins ID used follows the cmssw reccomandation:

    stxs_binName = {
          100: GG2H_FWDH,
          101: GG2H_PTH_GT200,
          102: GG2H_0J_PTH_0_10  ,
          103: GG2H_0J_PTH_GT10  ,
          104: GG2H_1J_PTH_0_60,
          105: GG2H_1J_PTH_60_120,
          106: GG2H_1J_PTH_120_200,
          107: GG2H_GE2J_MJJ_0_350_PTH_0_60,
          108: GG2H_GE2J_MJJ_0_350_PTH_60_120,
          109: GG2H_GE2J_MJJ_0_350_PTH_120_200,
          110: GG2H_MJJ_350_700_PTHJJ_0_25,
          111: GG2H_MJJ_350_700_PTHJJ_GT25,
          112: GG2H_MJJ_GT700_PTHJJ_0_25,
          113: GG2H_MJJ_GT700_PTHJJ_GT25,
    }
Plot for all relevant scale variations:

![stxs1p1](https://github.com/bonanomi/STXS_Unc/blob/master/STXS1p1_Unc.pdf)

## STXS 1.2
The bins ID used follows the cmssw reccomandation:

    stxs_binName = {
          100: 'GG2H_FWDH',
          101: 'GG2H_PTH_200_300',
          102: 'GG2H_PTH_300_450',
          103: 'GG2H_PTH_450_650',
          104: 'GG2H_PTH_GT650',
          105: 'GG2H_0J_PTH_0_10', 
          106: 'GG2H_0J_PTH_GT10', 
          107: 'GG2H_1J_PTH_0_60',
          108: 'GG2H_1J_PTH_60_120',
          109: 'GG2H_1J_PTH_120_200',
          110: 'GG2H_GE2J_MJJ_0_350_PTH_0_60',
          111: 'GG2H_GE2J_MJJ_0_350_PTH_60_120',
          112: 'GG2H_GE2J_MJJ_0_350_PTH_120_200',
          113: 'GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25',
          114: 'GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25',
          115: 'GG2H_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25',
          116: 'GG2H_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'
    }
Plot for all relevant scale variations:

![stxs1p2](https://github.com/bonanomi/STXS_Unc/blob/master/STXS1p2_Unc.pdf)
    

