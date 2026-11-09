"""Independent numerical check of the primary model only; not predictive validation."""
from pathlib import Path
import json, re
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.special import expit, logit
ROOT=Path(__file__).resolve().parents[1]
r=pd.read_excel(ROOT/'data/synthetic/updated_synthetic_data.xlsx')
d=r[r.a6n_emirati.isin(['Yes','No']) & r.a7_marital_status.isin(['Single','Engaged']) & (r.a3_gender!='Prefer not to answer') & (r.a2_age_group!='Prefer not to answer')].copy()
cols=['c1_employment_confidence','c9_housing_access','c14_financially_prepared','e3_family_support_confidence','e13_future_confidence','f9_worklife_balance']
d=d.dropna(subset=['b10_overall_family_readiness',*cols]);age=d.a2_age_group.str.replace(' years','').replace({'31-40':'31 or above','41-50':'31 or above','51 or above':'31 or above'})
x=np.column_stack([d[cols].to_numpy(float),d.a6n_emirati.eq('Yes'),d.a3_gender.eq('Male'),d.a4_role.eq('Employee'),age.eq('21-25'),age.eq('26-30'),age.eq('31 or above'),d.a0_survey_language.eq('Arabic'),d.a7_marital_status.eq('Engaged')]).astype(float)
y=d.b10_overall_family_readiness.to_numpy(int)-1;k=x.shape[1]
def nll(p):
 cuts=np.r_[p[k],p[k]+np.cumsum(np.exp(p[k+1:]))]
 c=expit(cuts[None,:]-(x@p[:k])[:,None]);pr=np.diff(np.column_stack([np.zeros(len(y)),c,np.ones(len(y))]),axis=1)
 return -np.log(np.maximum(pr[np.arange(len(y)),y],1e-300)).sum()
cuts=logit(np.cumsum(np.bincount(y,minlength=5)/len(y))[:-1]);start=np.r_[np.zeros(k),cuts[0],np.log(np.diff(cuts))]
f=minimize(nll,start,method='BFGS',options={'maxiter':2000,'gtol':1e-5})
# Confirm objective and rounded coefficients independently against supplied output.
text=(ROOT/'overleaf/ordinal_regression/table_ordinal.tex').read_text();reported=[]
for line in text.splitlines():
 parts=line.split(' & ')
 if len(parts)==6:
  try:reported.append(float(parts[1]))
  except ValueError:pass
err=float(np.max(np.abs(f.x[:k]-np.array(reported[:k]))));llerr=abs(-f.fun-(-428.38314818221363))
result={'scope':'Primary point estimates only, independently fitted with SciPy; not validation of other outputs','n':len(y),'log_likelihood':float(-f.fun),'max_difference_from_rounded_beta':err,'difference_from_reported_log_likelihood':llerr,'optimizer_message':str(f.message),'passed':bool(err<0.002 and llerr<0.0001),'odds_ratios':np.exp(f.x[:k]).tolist()}
out=ROOT/'checks';out.mkdir(exist_ok=True);(out/'independent_primary_check.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));assert result['passed']
