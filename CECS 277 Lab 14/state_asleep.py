import puppystate
import state_eat

class StateAsleep(puppystate.PuppyState):
  # Let the user know the puppy can't play while sleeping
  def play(self, puppy):
    return "The puppy is asleep. It doesn't want to play right now."

  def feed(self, puppy):
    #change state from sleeping to eating and reset feeds and plays
    puppy.change_state(state_eat.StateEat())
    puppy.reset()
    return "The puppy wakes up and comes running to eat."

