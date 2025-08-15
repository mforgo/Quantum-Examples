import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class ClassicalLBM1D:
    def __init__(self, nx, dt=1.0, dx=1.0):
        self.nx = nx
        self.dt = dt
        self.dx = dx
        self.velocities = np.array([-1, 1])
        self.weights = np.array([0.5, 0.5])
        self.f = np.zeros((nx, 2))
        self.f_new = np.zeros((nx, 2))
        self.density = np.zeros(nx)

    def set_initial_condition(self, density_func, velocity_func):
        x = np.arange(self.nx)
        dens = density_func(x)
        vel = velocity_func(x)
        self._compute_equilibrium(dens, vel)
        self.f = self.f_eq.copy()
        self.density = dens.copy()

    def _compute_equilibrium(self, dens, vel):
        self.f_eq = np.zeros((self.nx, 2))
        for i in range(self.nx):
            for k, c in enumerate(self.velocities):
                self.f_eq[i,k] = self.weights[k] * dens[i] * (1 + c * vel[i])

    def streaming(self):
        old_f = self.f.copy()
        self.f_new[:] = 0
        for k, c in enumerate(self.velocities):
            for i in range(self.nx):
                src = i - int(c)
                if src < 0 or src >= self.nx:
                    # bounce-back: reflect distribution
                    # left-going at left wall (i=0,k=0) comes from right at same site
                    # right-going at right wall (i=nx-1,k=1) comes from left at same site
                    self.f_new[i,k] = old_f[i,1-k]
                else:
                    self.f_new[i,k] = old_f[src,k]
        self.f[:] = self.f_new

    def collision(self, tau=1.0):
        dens = np.sum(self.f, axis=1)
        vel = np.sum(self.f * self.velocities, axis=1) / dens
        vel[np.isnan(vel)] = 0
        self._compute_equilibrium(dens, vel)
        self.f += -(1/tau)*(self.f - self.f_eq)

    def one_step_subframes(self, tau=1.0):
        self.streaming()
        dens_stream = np.sum(self.f, axis=1).copy()
        self.collision(tau)
        dens_col = np.sum(self.f, axis=1).copy()
        return dens_stream, dens_col

def create_gaussian_pulse(x, center, width, amplitude=1.0):
    return amplitude * np.exp(-((x-center)/width)**2)

def main():
    nx = 128
    n_steps = 1000
    tau = 1.2

    lbm = ClassicalLBM1D(nx)
    lbm.set_initial_condition(
        lambda x: create_gaussian_pulse(x, nx//4, 5.0, 2.0),
        lambda x: np.full_like(x, 0.2)
    )

    subframes = []
    for _ in range(n_steps):
        s, c = lbm.one_step_subframes(tau)
        subframes.append(s)
        subframes.append(c)
    subframes = np.array(subframes)

    fig, ax = plt.subplots()
    line, = ax.plot(subframes[0], color='blue')
    ax.set_xlim(0, nx-1)
    ax.set_ylim(0, subframes.max()*1.1)
    ax.set_xlabel('Position')
    ax.set_ylabel('Density')

    def update(frame):
        line.set_ydata(subframes[frame])
        ax.set_title(f'Sub-frame {frame+1}/{len(subframes)}')
        return line,

    anim = animation.FuncAnimation(
        fig, update, frames=len(subframes), interval=50, blit=True

    )

    plt.show()

if __name__ == "__main__":
    main()
