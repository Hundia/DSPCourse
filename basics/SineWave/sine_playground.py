import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots


# Function to generate sine wave data
def generate_sine_wave(amplitude, frequency, phase, duration):
    t = np.linspace(0, duration, 1000)
    x = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return t, x


# Parameters for sine waves
parameters = [
    (1, 1, 0, 'Amplitude=1, Frequency=1Hz, Phase=0'),
    # (2, 1, 0, 'Amplitude=2, Frequency=1Hz, Phase=0'),
    # (1, 2, 0, 'Amplitude=1, Frequency=2Hz, Phase=0'),
    # (1, 1, np.pi / 4, 'Amplitude=1, Frequency=1Hz, Phase=π/4'),
    # (1, 1, np.pi / 2, 'Amplitude=1, Frequency=1Hz, Phase=π/2')
]

# Create a subplot
fig = make_subplots(rows=1, cols=1)

# Plot each sine wave with different parameters
colors = ['blue', 'green', 'red', 'purple', 'orange']
for i, (amplitude, frequency, phase, label) in enumerate(parameters):
    t, x = generate_sine_wave(amplitude, frequency, phase, 2)
    fig.add_trace(go.Scatter(x=t, y=x, mode='lines', name=label, line=dict(color=colors[i])))

    # Annotate amplitude
    max_amplitude_time = (np.pi - phase) / (2 * np.pi * frequency)
    # if 0 <= max_amplitude_time < 2:
    #     fig.add_annotation(x=max_amplitude_time, y=amplitude, text=f'Amplitude = {amplitude}', showarrow=True,
    #                        arrowhead=1)
    #
    # # Annotate phase
    # fig.add_annotation(x=0, y=np.sin(phase) * amplitude, text=f'Phase = {phase:.2f}', showarrow=True, arrowhead=1,
    #                    ax=40)

# Update layout
fig.update_layout(title='Interactive Sine Waves with Different Parameters',
                  xaxis_title='Time (s)',
                  yaxis_title='Amplitude',
                  showlegend=True)

# Show the plot
fig.show()
