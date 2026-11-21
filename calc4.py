import math
from CoolProp.CoolProp import PropsSI as P
g=9.80665
def cushion(m,v1,v2,h,Isp=250):
    a=(v1**2-v2**2)/(2*h); F=m*(a+g); t=(v1-v2)/a; I=F*t; return a/g,F,t,I,I/(Isp*g)
for name,m,v1,v2,h in [("drone 25 kg 12->1 em 3 m",25,12,1,3),("drone 25 kg paraq 6->1 em 0,5 m",25,6,1,0.5),
 ("eVTOL 2.500 kg paraq 8->2 em 1 m",2500,8,2,1),("eVTOL 2.500 kg 15->3 em 5 m",2500,15,3,5),
 ("C172 1.157 paraq 8->2 em 1 m",1157,8,2,1),("SR22 1.633 paraq 8->2 em 1 m",1633,8,2,1),
 ("Caravan 3.900 paraq 8->2 em 1 m",3900,8,2,1),("Caravan 3.900 15->3 em 5 m",3900,15,3,5)]:
    G,F,t,I,mp=cushion(m,v1,v2,h); print(f"{name}: {G:.1f} g, F {F/1e3:.1f} kN, t {t:.2f} s, I {I/1e3:.1f} kN.s, prop {mp:.1f} kg, sist {mp/0.8:.1f} kg")
for p in (300e5,690e5): print('N2',p/1e5,'bar dens',round(P('D','P',p,'T',293.15,'Nitrogen')))
# Caravan spin recovery yaw
b=15.87; L=12.67; m=3900
Izz=((b+L)/2)**2*m*0.44**2/4; print('Caravan Izz',round(Izz))
for w,ts in [(1.0,2.0),(1.5,2.0)]:
    alpha=w/ts; M=Izz*alpha; F=M/(b/2); print('spin',w,'rad/s em',ts,'s: M',round(M/1e3,1),'kN.m F',round(F/1e3,2),'kN')
# impulse budget: 2 nozzle sets yaw 3 kN for 4 s + pitch 2 kN for 3 s, margin 2
I=(3e3*4+2e3*3)*2; ve=580; mu=I/ve; print('budget I kN.s',I/1e3,'N2 usable kg',round(mu),'stored(50%)',round(mu/0.5))
for p,d in [(300e5,P('D','P',300e5,'T',293.15,'Nitrogen'))]:
    V=mu/0.5/d; print('vol L @300bar',round(V*1000))
    for pvw in (1e4,2.5e4): print(' tank kg',round(p*V/(pvw*g)))
# C172 Izz and spin
b=11.0; L=8.28; m=1157; Izz=((b+L)/2)**2*m*0.39**2/4; print('C172 Izz',round(Izz), 'F for 1 rad/s in 2 s at 5.5 m', round(Izz*0.5/5.5),'N')
# hover impossible check eVTOL
print('eVTOL hover thrust kN', 2500*g/1e3)
