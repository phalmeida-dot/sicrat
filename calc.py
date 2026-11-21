import math
g=9.80665; R=287.053; g0=9.80665
def isa(h):
    if h<=11000:
        T=288.15-0.0065*h; p=101325*(T/288.15)**(g/(R*0.0065))
    else:
        T=216.65; p=22632.06*math.exp(-g*(h-11000)/(R*T))
    rho=p/(R*T); a=math.sqrt(1.4*R*T); return T,p,rho,a
for h in [0,3000,10000,11000,12000]:
    T,p,rho,a=isa(h); print(h, round(T-273.15,1), round(p), round(rho,4), round(rho/1.225*100,1),'%', round(a,1))
# q values
for name,h,V in [("cruzeiro M0.78 10.7km",10668,None),("aprox 70m/s SL",0,70),("estol alt 12km ~ M0.6",12000,None)]:
    T,p,rho,a=isa(h)
    if V is None: V=(0.78 if '0.78' in name else 0.6)*a
    print(name, round(V,1), 'q=',round(0.5*rho*V*V))
# total temp at M0.78 12km
T,p,rho,a=isa(10668); print('Ttotal M0.78', round(T*(1+0.2*0.78**2)-273.15,1), 'Tstatic', round(T-273.15,1))
# retro cushion
def cushion(m,v1,v2,h,Isp=250,frac=0.8):
    a=(v1**2-v2**2)/(2*h); F=m*(a+g); t=(v1-v2)/a; I=F*t; mp=I/(Isp*g0); return a,F,t,I,mp,mp/frac
cases=[("Cessna 172 (1.157 kg) 15→3 m/s em 5 m",1157,15,3,5),
("Cirrus SR22 sob paraquedas (1.633 kg) 8→2 m/s em 1 m",1633,8,2,1),
("ATR 72 (23.000 kg) 15→3 m/s em 10 m",23000,15,3,10),
("A320 (65.000 kg) 10→3 m/s em 10 m",65000,10,3,10),
("A320 (65.000 kg) 15→3 m/s em 10 m",65000,15,3,10),
("A320 (65.000 kg) 15→3 m/s em 30 m",65000,15,3,30),
("A320 (65.000 kg) 25→3 m/s em 30 m",65000,25,3,30),
("A330 AF447 (205.000 kg) 55→5 m/s em 100 m",205000,55,5,100),
("ATR 72 Vinhedo (21.000 kg) 71→5 m/s em 150 m",21000,71,5,150),
]
for c in cases:
    a,F,t,I,mp,mt=cushion(*c[1:])
    print(c[0], f"a={a:.1f} m/s2 ({a/g:.2f} g) F={F/1e3:.0f} kN t={t:.2f}s I={I/1e3:.0f} kN.s prop={mp:.0f} kg sistema~{mt:.0f} kg")
# horizontal kill
for m,v,tb in [(65000,70,3),(65000,70,5)]:
    I=m*v; mp=I/(250*g0); print('horiz',m,v,tb,'I',I/1e6,'MN.s prop',round(mp),'decel g',round(v/tb/g,2),'F MN',round(m*v/tb/1e6,2))
# energy
print('Ek/kg 70 m/s',0.5*70**2,' 15 m/s vert',0.5*15**2, 'ratio', 70**2/15**2)
# dive stop 250 m/s
print('stop 250m/s A320 prop', round(65000*250/(250*g0)))
# pitch inertia Roskam
for name,L,m,Ry in [("A320",37.57,65000,0.38),("ATR72",27.17,21000,0.37),("C172",8.28,1100,0.338)]:
    Iyy=L**2*m*Ry**2/4; print(name,'Iyy',f"{Iyy:.3g}")
Iyy=37.57**2*65000*0.38**2/4
alpha=math.radians(3); M=Iyy*alpha; F=M/17; print('A320 3deg/s2 M',round(M/1e3),'kN.m F@17m',round(F/1e3,1),'kN')
# arrest 5 deg/s in 2 s + hold 10 s
alpha=math.radians(5)/2; M=Iyy*alpha; F=M/17; I=F*10; print('arrest 5deg/s in 2s: M',round(M/1e3),'kN.m F',round(F/1e3,1),'kN; 10 s impulse',round(I/1e3),'kN.s prop',round(I/(250*g0),1),'kg')
# tail aero moment cruise
T,p,rho,a=isa(10668); V=0.78*a; q=0.5*rho*V*V; St=31; lt=17; dCL=0.3
Ft=q*St*dCL; print('cruise q',round(q),'tail force dCL0.3',round(Ft/1e3),'kN moment',round(Ft*lt/1e3),'kN.m')
# low q deep stall: 12 km V=100 m/s
T,p,rho,a=isa(12000); q2=0.5*rho*100**2; print('q 12km 100 m/s', round(q2), 'tail force',round(q2*St*dCL/1e3),'kN')
# fuel penalty
for mt in [200,500,800]:
    dfuel=mt*5000/65000; yr=dfuel*1500; print(mt,'kg -> per 2h flight',round(dfuel),'kg fuel; per yr',round(yr/1000),'t; CO2 t',round(yr*3.16/1000),'; US$ @0.8/kg',round(yr*0.8))
# thrust altitude gain example: Ae=0.05 m2
Ae=0.05; print('thrust gain SL->12km Ae 0.05m2', round((101325-19330)*Ae),'N')
# cold gas
print('cold gas N2 Isp 70: prop for 15->3 C172', round(19.4e3/(70*g0)))
# cold pressure drop
print('pressure ratio -56.5/+15', round(216.65/288.15,3))
