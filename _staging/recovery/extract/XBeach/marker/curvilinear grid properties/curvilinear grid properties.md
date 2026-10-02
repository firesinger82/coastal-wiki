

{0}------------------------------------------------

{1}------------------------------------------------

{2}------------------------------------------------

{3}------------------------------------------------

{4}------------------------------------------------

{5}------------------------------------------------

{6}------------------------------------------------

{7}------------------------------------------------

{8}------------------------------------------------

{9}------------------------------------------------

{10}------------------------------------------------

## Momentum balance in u direction

 Only consider advection of velocity component in the local grid direction

$$\frac{d(\nabla u)}{dt} - \sum_{i=1}^{N} Q_{in} u_{in} + \sum_{i=1}^{N} Q_{out} u + Vg \frac{\partial \eta}{\partial s} + A \frac{\tau_{b,s}}{\rho} = 0 \Rightarrow$$

$$u \frac{dV}{dt} + V \frac{du}{dt} - \sum_{i=1}^{N} Q_{in} u_{in} + \sum_{i=1}^{N} Q_{out} u + Vg \frac{\partial \eta}{\partial s} + A \frac{\tau_{b,s}}{\rho} = 0$$

{11}------------------------------------------------

### Continuity equation

$$\frac{dV}{dt} - \sum Q_{in} + \sum Q_{out} = 0$$

Multiply continuity equation with u

$$u\frac{dV}{dt} - \sum Q_{in}u + \sum Q_{out}u = 0$$

{12}------------------------------------------------

 Subtract continuity eq. times u from momentum equation and divide by V

$$V\frac{du}{dt} + \sum Q_{in}(u - u_{in}) + Vg\frac{\partial \eta}{\partial s} + A\frac{\tau_{b,s}}{\rho} = 0$$

$$\frac{du}{dt} + \frac{\sum Q_{in}(u - u_{in})}{V} + g\frac{\partial \eta}{\partial s} + \frac{A\tau_{b,s}}{\rho V} = 0$$

$$\frac{du}{dt} + \frac{\sum Q_{in}(u - u_{in})}{Ah_{um}} + g\frac{\partial \eta}{\partial s} + \frac{\tau_{b,s}}{\rho h_{um}} = 0$$

{13}------------------------------------------------

#### Procedure

- Go around the cell centered at upoint
- Compute q across cell boundary by averaging qx resp. qy
- If q is inward
  - Compute  $Q_{in}$  by  $m_{u}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$   $d_{in}$
  - Compute u<sub>in</sub> as

– Add Q<sub>in</sub> (u<sub>in</sub> –u) to advection

{14}------------------------------------------------

{15}------------------------------------------------

{16}------------------------------------------------

# Water level slopes in u, v points

$$\frac{\partial \eta}{\partial s}(i,j) = \frac{\eta_{i+1,j} - \eta_{i,j}}{dsu_{i,j}}$$

$$\frac{\partial \eta}{\partial n}(i,j) = \frac{\eta_{i,j+1} - \eta_{i,j}}{dnv_{i,j}}$$

{17}------------------------------------------------

### Continuity

$$\frac{\eta_{i,j}^{n+1} - \eta_{i,j}^n}{\Delta t} =$$

$$\frac{\left(u_{i,j}^{n+1}h_{i,j}^{n}dnu_{i,j}-u_{i-1,j}^{n+1}h_{i-1,j}^{n}dnu_{i-1,j}\right)-\left(v_{i,j}^{n+1}h_{i,j}dsv_{i,j}-v_{i,j-1}^{n+1}h_{i,j-1}^{n}dsv_{i,j-1}\right)}{dsdnz_{i,j}}$$

{18}------------------------------------------------

### Wave propagation

$$\begin{split} &Cgxu_{i,j} = \frac{1}{2}(Cgx_{i,j} + Cgx_{i+1,j}) \\ &Eu_{i,j} = E_{i,j} + \frac{1}{2}dsu_{i,j}\frac{E_{i,j} - E_{i-1,j}}{dsu_{i-1,j}} = \\ &= \left( \left( dsu_{i-1,j} + \frac{1}{2}dsu_{i,j} \right) E_{i,j} - \frac{1}{2}dsu_{i,j} E_{i-1,j} \right) / dsu_{i-1,j} \quad , Cgxu_{i,j} > 0 \\ &Eu_{i,j} = E_{i+1,j} - \frac{1}{2}dsu_{i,j}\frac{E_{i+2,j} - E_{i+1,j}}{dsu_{i+1,j}} = \\ &= \left( \left( dsu_{i+1,j} + \frac{1}{2}dsu_{i,j} \right) E_{i+1,j} - \frac{1}{2}dsu_{i,j} E_{i+2,j} \right) / dsu_{i+1,j} \quad , Cgxu_{i,j} < 0 \\ &Fluxx_{i,j} = Cgxu_{i,j}Eu_{i,j}dnu_{i,j} \end{split}$$