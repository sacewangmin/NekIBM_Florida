import numpy as np
from netCDF4 import Dataset
import netCDF4
import matplotlib.pyplot as plt


#-------------------------------------------------------------------------------

newa = np.loadtxt('hydrodynamic_forces.txt')


m=0
n = len(newa)
print(n)


# First priciple stress
#plt.plot(newa[m:n,0],ara[0:n-m],c='b',ms=5,marker='v',markevery=10,mfc='w')
#plt.plot(newb[m:n,0],bra[0:n-m],c='g',ms=5,marker='v',markevery=10,mfc='w')
#plt.plot(newc[m:n,0],cra[0:n-m],c='y',ms=5,marker='v',markevery=10,mfc='w')
#plt.plot(newd[m:n,0],dra[0:n-m],c='r',ms=5,marker='v',markevery=10,mfc='w')
#plt.plot(newe[m:n,0],era[0:n-m],c='k',ms=5,marker='v',markevery=10,mfc='w')

plt.plot(newa[m:n,0],newa[m:n,1],c='k',ms=5,marker='o',markevery=10,mfc='w')
plt.plot(newa[m:n,0],newa[m:n,2],c='b',ms=5,marker='v',markevery=10,mfc='w')
plt.plot(newa[m:n,0],newa[m:n,3],c='r',ms=5,marker='d',markevery=10,mfc='w')


plt.xlabel('Time Steps (-)')
plt.ylabel('Hydrodynamic force (-)')
plt.grid(True)
plt.xticks(color='k')
plt.yticks(color='k')
plt.legend(('Fx','Fy','Fz'))
plt.show()


plt.plot(newa[m:n,0],newa[m:n,1],c='k',ms=5,marker='o',markevery=10,mfc='w')

plt.plot(newa[m:n,0],newa[m:n,3],c='r',ms=5,marker='d',markevery=10,mfc='w')


plt.xlabel('Time Steps (-)')
plt.ylabel('hydrodynamic force (-)')
plt.grid(True)
plt.xticks(color='k')
plt.yticks(color='k')
plt.legend(('Fx','Fz'))
plt.show()

plt.plot(newa[m+600:n,0],newa[m+600:n,2],c='b',ms=5,marker='v',markevery=10,mfc='w')
plt.xlabel('Time Steps (-)')
plt.ylabel('Drag force (-)')
plt.grid(True)
plt.xticks(color='k')
plt.yticks(color='k')
plt.legend(('Fy'))
plt.show()

print(newa[-1:n,2], newa[-1:n,2]/0.00000422)

plt.plot(newa[m+600:n,0],newa[m+600:n,2]/0.00000422,c='b',ms=5,marker='v',markevery=10,mfc='w')
plt.xlabel('Time Steps (-)')
plt.ylabel('Cd/Cd0 (-)')
plt.grid(True)
plt.xticks(color='k')
plt.yticks(color='k')
plt.legend(('Cd'))
plt.show()
