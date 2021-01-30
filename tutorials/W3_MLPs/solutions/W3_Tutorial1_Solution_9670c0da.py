
def run_LIF(I, T = 50, dt = 0.1, t_rest = 0, tau_ref = 4,
            Rm = 1, Cm = 10, Vth = 1, V_spike = 0.5):
  """
  Simulate the LIF dynamics with external input current

  Args:
    I          : input current (mA)
    T          : total time to simulate (msec)
    dt         : simulation time step (msec)
    t_rest     : initial refractory time
    tau_ref    : refractory period (msec)
    Rm         : resistance (kOhm)
    Cm         : capacitance (uF)
    Vth        : spike threshold (V)
    V_spike    : spike delta (V)

  Returns:
    time       : time points
    Vm         : membrane potentials
  """

  # Set up array of time steps
  time = torch.arange(0, T+dt, dt)

  # Set up array for tracking Vm
  Vm = torch.zeros(len(time))

  # Iterate over each time step
  for i, t in enumerate(time):

    # If t is after refractory period
    if t > t_rest:
      Vm[i] = Vm[i-1] + 1/Cm*(-Vm[i-1]/Rm + I)  * dt

    # If Vm is over the threshold
    if Vm[i] >= Vth:

      # Increase volatage by change due to spike
      Vm[i] += V_spike

      # Set up new refactory period
      t_rest = t + tau_ref

  return time, Vm


### Uncomment below to test your function
sim_time, Vm = run_LIF(1.5)
with plt.xkcd():
  plt.plot(sim_time, Vm)
  plt.title('LIF Neuron Output')
  plt.ylabel('Membrane Potential (V)')
  plt.xlabel('Time (msec)')
  plt.show()