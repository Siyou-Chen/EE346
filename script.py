import random

def sample_particles():
    particles = {'1': 0.1, '2': 0.2, '3': 0.7}
    sampled_particles = random.choices(list(particles.keys()), weights=list(particles.values()), k=3)
    return sampled_particles



if __name__ =='__main__':
    for i in range(5):
        result = sample_particles()
        print(f"Experiment {i + 1}: {result}")