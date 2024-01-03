# NavierStokes 方程常用时间积分方法

本文档总结 NavierStokes 方程的常用时间积分方法

考虑

$$
\begin{equation}
\begin{aligned}
    &\mathbf{u}_t - \nu \Delta \mathbf{u} + \nabla p + \mathbf{u} \cdot \nabla \mathbf{u} = \mathbf{f}, \\ 
    &\nabla \cdot \mathbf{u} = 0.
\end{aligned}
\end{equation}
$$

## 耦合格式

### 全隐格式

$$
\begin{equation}
\begin{aligned}
    &\frac{\mathbf{u}^{n+1}-\mathbf{u}^n}{\tau} - \nu \Delta \mathbf{u}^{n+1} + \nabla p^{n+1} + \mathbf{u}^{n+1} \cdot \nabla \mathbf{u}^{n+1} = \mathbf{f}(t_{n+1}), \\ 
    &\nabla \cdot \mathbf{u}^{n+1} = 0. 
\end{aligned}
\end{equation}
$$

### 完全显式处理非线性项的半隐格式

$$
\begin{equation}
\begin{aligned}
    & \frac{\mathbf{u}^{n+1} - \mathbf{u}^n}{\tau} - \nu \Delta \mathbf{u}^{n+1} + \nabla p^{n+1} + \mathbf{u}^n \cdot \nabla \mathbf{u}^n = \mathbf{f}(t_{n+1}), \\
    & \nabla \cdot \mathbf{u}^{n+1} = 0.
\end{aligned}
\end{equation}
$$

求解:

$$
\begin{equation}
\begin{aligned}
    & -\nu \Delta \mathbf{u}^{n+1} + \nabla p^{n+1} + \frac{\mathbf{u}^{n+1}}{\tau} = \mathbf{f}(t_{n+1}) + \frac{\mathbf{u}^n}{\tau} - \mathbf{u}^n \cdot \nabla \mathbf{u}^n, \\ 
    &\nabla \cdot \mathbf{u}^{n+1} = 0.
\end{aligned}
\end{equation}
$$

## 解耦格式

### 压力校正格式

$$
\begin{equation}
\begin{aligned}
    & \frac{\widetilde{\mathbf{u}}-\mathbf{u}^n}{\tau} - \nu \Delta \widetilde{\mathbf{u}} + \nabla p^n + \mathbf{u}^n \cdot \nabla \widetilde{\mathbf{u}} = \mathbf{f}(t_{n+1}), \\ 
    & \widetilde{\mathbf{u}}|_{\partial \Omega} = 0,
\end{aligned}
\end{equation}
$$
$$
\begin{equation}
\begin{aligned}
    & \frac{\mathbf{u}^{n+1} - \widetilde{\mathbf{u}}}{\tau} + \nabla(p^{n+1} - p^n) = 0, \\ 
    & \nabla \cdot \mathbf{u}^{n+1} = 0, \\ 
    & \mathbf{u}^{n+1} \cdot \mathbf{n} = 0.
\end{aligned}
\end{equation}
$$

求解:

$$
\begin{equation}
\begin{aligned}
    & \left( -\nu \Delta + \mathbf{u}^n \cdot \nabla + \frac{1}{\tau} \right) \widetilde{\mathbf{u}} = \frac{\mathbf{u}^n}{\tau} - \nabla p^n + \mathbf{f}(t_{n+1}), \\ 
    & \widetilde{\mathbf{u}} |_{\partial \Omega} = 0,
\end{aligned}
\end{equation}
$$
$$
\begin{equation}
\begin{aligned}
    & - \Delta p^{n+1} = -\Delta p^n - \frac{\nabla \cdot \widetilde{\mathbf{u}}}{\tau}, \\ 
    & \nabla p^{n+1} \cdot \mathbf{n} = 0.
\end{aligned}
\end{equation}
$$