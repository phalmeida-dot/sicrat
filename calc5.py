"""SICRAT v5: limites de uso (recursos finitos) e cenário de gelo. Estimativas [E]."""
import json, math
g=9.80665
# Roskam: I = b^2 * m * R^2 / 4 (Rx~0.248, Rz~0.391 monomotor) ; Izz Caravan/C172 de calc4
AC={
 "drone":  dict(nome="Drone de carga 25 kg", m=25,   b=2.0,  Izz=5.0,   arm=0.8,  budget=0.10, jet=0.025, spin_sink=12, chute_v=6,  retro=dict(v1=12,v2=1,h=3)),
 "c172":   dict(nome="Cessna 172",           m=1157, b=11.0, Izz=4088,  arm=5.5,  budget=5.8,  jet=0.5,   spin_sink=30, chute_v=8,  retro=dict(v1=8,v2=2,h=1)),
 "sr22":   dict(nome="Cirrus SR22",          m=1633, b=11.7, Izz=6530,  arm=5.85, budget=8.0,  jet=0.7,   spin_sink=32, chute_v=8,  retro=dict(v1=8,v2=2,h=1)),
 "evtol":  dict(nome="eVTOL 2,5 t",          m=2500, b=12.0, Izz=10000, arm=6.0,  budget=8.0,  jet=1.0,   spin_sink=25, chute_v=8,  retro=dict(v1=8,v2=2,h=1)),
 "caravan":dict(nome="Cessna 208B Caravan",  m=3900, b=15.88,Izz=38438, arm=7.9,  budget=36.0, jet=3.0,   spin_sink=40, chute_v=8,  retro=dict(v1=8,v2=2,h=1)),
}
out={}
for k,a in AC.items():
    Ixx=a["b"]**2*a["m"]*0.248**2/4
    fire=a["budget"]/a["jet"]                 # s de jato a empuxo nominal
    pulses=int(fire/0.5)
    t_stop=a["Izz"]*1.0/(a["jet"]*1000*a["arm"])  # parar 1 rad/s
    stops=a["budget"]*1000/(a["Izz"]*1.0/a["arm"])
    n=2.5
    loss=(1.0+t_stop)*a["spin_sink"] + a["spin_sink"]**2/(g*(n-1))
    hmin=1.5*loss
    r=a["retro"]; acc=(r["v1"]**2-r["v2"]**2)/(2*r["h"]); F=a["m"]*(acc+g); tb=(r["v1"]-r["v2"])/acc; I=F*tb; mp=I/(250*g)
    crush=0.3
    g_with=r["v2"]**2/(2*crush*g); g_without=r["v1"]**2/(2*crush*g)
    out[k]=dict(nome=a["nome"],m=a["m"],Ixx=round(Ixx),Izz=a["Izz"],arm=a["arm"],budget_kNs=a["budget"],jet_kN=a["jet"],
        fire_s=round(fire,1),pulses_05s=pulses,t_stop_1rads=round(t_stop,2),stops_1rads=round(stops,1),
        spin_sink=a["spin_sink"],hmin_spin_m=round(hmin),hmin_spin_ft=round(hmin/0.3048,-1),
        retro_v1=r["v1"],retro_v2=r["v2"],retro_h=r["h"],retro_F_kN=round(F/1000,1),retro_burn_s=round(tb,2),retro_I_kNs=round(I/1000,2),retro_mp_kg=round(mp,2),
        impact_g_with=round(g_with,1),impact_g_without=round(g_without,1))
# Gelo: Caravan com aileron travado
c=out["caravan"]; Ixx=c["Ixx"]; Mj=3500.0
alpha=Mj/Ixx; t60=math.sqrt(2*math.radians(60)/alpha)
Fjet=Mj/c["arm"]  # um bocal na ponta (N)
T_pilot=15.0
use=Fjet*T_pilot/2/1000  # pilot ramps linearly -> gas covers triangle
ice=dict(Ixx=Ixx,Mj_Nm=Mj,alpha=round(alpha,3),t_bank60_s=round(t60,1),Fjet_N=round(Fjet),T_pilot_s=T_pilot,gas_kNs=round(use,1),gas_frac=round(use/c["budget_kNs"],2),
         hold_max_s=round(c["budget_kNs"]*1000/Fjet,0),stall_rise=round(1/math.sqrt(0.7)-1,2))
out["_gelo"]=ice
json.dump(out,open("limites.json","w"),ensure_ascii=False,indent=1)
for k,v in out.items(): print(k,v)
