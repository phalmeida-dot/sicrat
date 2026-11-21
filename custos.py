# Modelo de custos SICRAT v3 — todas as linhas são estimativas [E] com faixas (baixo, alto)
import json, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
LAB=(120,180)      # US$/h mão de obra MRO [E]
FUEL=(0.65,0.90)   # US$/kg combustível [E]
RULE=(0.025,0.04)  # kg comb. por kg extra por hora de voo [E, regra 2,5-4%/h]
types=[
 # nome, frota, massa sistema kg, hardware US$, horas instalação, STC/cert por tipo US$, downtime dias, horas voo/ano, manut US$/ano
 ("737-800/MAX",7688,(800,1500),(1.0e6,3.0e6),(3000,8000),(80e6,250e6),(14,28),(3000,4000),(15e3,40e3)),
 ("A320ceo/neo",10310,(800,1500),(1.0e6,3.0e6),(3000,8000),(80e6,250e6),(14,28),(3000,4000),(15e3,40e3)),
 ("E-Jets (E175/E195)",747,(500,900),(0.6e6,1.8e6),(2000,5000),(50e6,150e6),(10,21),(2500,3200),(10e3,30e3)),
 ("ATR 72-600",891,(400,800),(0.4e6,1.0e6),(1500,3000),(20e6,60e6),(10,21),(2000,2500),(8e3,20e3)),
 ("Caravan 208B",2500,(150,300),(80e3,200e3),(150,300),(3e6,10e6),(5,10),(600,1200),(2e3,6e3)),
 ("SR22 (módulo retro + CAPS existente)",8000,(10,20),(8e3,20e3),(20,40),(0.5e6,2e6),(3,7),(100,200),(300,900)),
 ("C172 (BRS + módulo retro)",20000,(45,60),(37e3,55e3),(60,100),(0.5e6,2e6),(5,10),(100,200),(800,1500)),
]
rows=[]
for n,fleet,m,hw,h,stc,dt,fh,mt in types:
    lo_inst=hw[0]+h[0]*LAB[0]; hi_inst=hw[1]+h[1]*LAB[1]
    fuel_lo=m[0]*RULE[0]*fh[0]*FUEL[0]; fuel_hi=m[1]*RULE[1]*fh[1]*FUEL[1]
    rows.append(dict(tipo=n,frota=fleet,massa=m,unid=(lo_inst,hi_inst),stc=stc,dias=dt,comb=(fuel_lo,fuel_hi),manut=mt,
        frota_total=(fleet*lo_inst+stc[0],fleet*hi_inst+stc[1]),frota_comb=(fleet*fuel_lo,fleet*fuel_hi)))
def M(x): return f"{x/1e6:,.1f}".replace(",","X").replace(".",",").replace("X",".")
for r in rows:
    print(f"{r['tipo']}: unid US$ {r['unid'][0]/1e3:.0f}k-{r['unid'][1]/1e3:.0f}k | STC {M(r['stc'][0])}-{M(r['stc'][1])} mi | comb/ano {r['comb'][0]/1e3:.1f}k-{r['comb'][1]/1e3:.1f}k | frota {r['frota_total'][0]/1e9:.2f}-{r['frota_total'][1]/1e9:.2f} bi | comb frota/ano {r['frota_comb'][0]/1e6:.0f}-{r['frota_comb'][1]/1e6:.0f} mi")
# narrowbody combined
nb=[r for r in rows if r['tipo'] in ("737-800/MAX","A320ceo/neo")]
print('NB total bi', sum(r['frota_total'][0] for r in nb)/1e9, sum(r['frota_total'][1] for r in nb)/1e9, 'comb/ano bi', sum(r['frota_comb'][0] for r in nb)/1e9, sum(r['frota_comb'][1] for r in nb)/1e9)
# linefit
NRE=(0.3e9,1.0e9); unit=(0.5e6,1.5e6); units=(2000,6000)
amort=(NRE[0]/units[1],NRE[1]/units[0]); print('amort/unit',amort)
prem=(unit[0]+amort[0], unit[1]+amort[1]); print('premium base',prem,'with margin 30%',(prem[0]*1.3,prem[1]*1.3))
# benefit
VSL=13.7e6; locdeaths=995/10
for share in (0.1,0.3): print('benefit/yr share',share, locdeaths*share*VSL/1e9,'bi')
json.dump(rows,open('custos.json','w'),default=list,ensure_ascii=False,indent=1)
# charts
names=[r['tipo'].split(' (')[0] for r in rows]
fig,ax=plt.subplots(figsize=(8,4))
for i,r in enumerate(rows):
    ax.plot([r['unid'][0]/1e3,r['unid'][1]/1e3],[i,i],lw=8,color='#3b6fd8',solid_capstyle='butt')
ax.set_xscale('log'); ax.set_yticks(range(len(rows))); ax.set_yticklabels(names); ax.invert_yaxis()
ax.set_xlabel('US$ mil por aeronave (escala log) — estimativa [E]'); ax.set_title('Retrofit: custo por aeronave (peças + instalação)')
ax.grid(axis='x',alpha=.3); plt.tight_layout(); plt.savefig('fig/retrofit_unit.png',dpi=160); plt.close()
fig,ax=plt.subplots(figsize=(8,4))
for i,r in enumerate(rows):
    ax.plot([r['comb'][0]/1e3,r['comb'][1]/1e3],[i,i],lw=8,color='#e0a020',solid_capstyle='butt')
ax.set_xscale('log'); ax.set_yticks(range(len(rows))); ax.set_yticklabels(names); ax.invert_yaxis()
ax.set_xlabel('US$ mil por aeronave por ano (escala log) — [E]'); ax.set_title('Combustível extra pelo peso do sistema')
ax.grid(axis='x',alpha=.3); plt.tight_layout(); plt.savefig('fig/fuel_year.png',dpi=160); plt.close()
# propellant chart from v1
cases=[("SR22+paraq. 8→2 m/s/1 m",5),("C172 15→3/5 m",8),("ATR 72 15→3/10 m",215),("A320 10→3/10 m",586),("A320 15→3/10 m",607),("ATR Vinhedo 71→5/150 m",897),("A320 25→3/30 m",1140),("A330 AF447 55→5/100 m",6914)]
fig,ax=plt.subplots(figsize=(8,4)); ax.barh([c[0] for c in cases],[c[1] for c in cases],color='#3b6fd8'); ax.set_xscale('log'); ax.invert_yaxis()
for i,c in enumerate(cases): ax.text(c[1]*1.1,i,f"{c[1]:,} kg".replace(",","."),va='center',fontsize=8)
ax.set_xlabel('kg de propelente sólido (Isp 250 s, escala log) — [E]'); ax.set_title('Retrofoguetes: propelente para amortecer a queda'); plt.tight_layout(); plt.savefig('fig/propelente.png',dpi=160); plt.close()
# ISA
alts=[0,3,10,11,12]; dens=[100,74,34,30,25]
fig,ax=plt.subplots(figsize=(6,3)); ax.plot(alts,dens,'o-',color='#3b6fd8'); ax.set_xlabel('altitude (km)'); ax.set_ylabel('% densidade ao nível do mar'); ax.set_title('Ar rarefeito (ISA)'); ax.grid(alpha=.3); plt.tight_layout(); plt.savefig('fig/isa.png',dpi=160); plt.close()
