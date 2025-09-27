

![[Introduction_to_Quantum_Computing-GDC notes.pdf]]


$$
\begin{align}
& z = a +ib \\
& z = \rho(cos\theta+isin\theta) = \rho*e^{i\theta} \\ \\
& |z|^2 = z * z^* = a^2+b^2 = \rho^2 = |z^*|^2 \\ \\
& z^* = a - ib
\end{align}
$$

$\rho$ = distanza dall'origine = "modulus"

$\theta$ = angolo formato con gli assi reali positivi

$e^{i\theta}$ = phase

$z^*$ = complex conjugate of z

![Euler's Identity](image.png)

$z^n - 1 = 0 \implies \text{ n solutions aka n roots of Unity}$

$\omega_n = e^{\frac{2\pi * i}{n}} = \cos{\frac{2\pi}{n}} + i * \sin{\frac{2\pi}{n}}$

$\omega_n$ indica nth root

Properties:
- $\omega_n^k = e^{\frac{2\pi*i*k}{n}} = (\cos{\frac{2\pi}{n}} + i * \sin{\frac{2\pi}{n}})^k$
- $\omega_n^0 = 1$
- $\omega_n^{n+k} = \omega_n^n * \omega_n^k = \omega_n^k$
- $\omega_n^{n+k} = \omega_n^n * \omega_n^-k = \omega_n^-k$
