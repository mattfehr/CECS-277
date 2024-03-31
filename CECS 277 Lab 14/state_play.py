import puppystate
import state_asleep

class StatePlay(puppystate.PuppyState):
  # Let the user know the puppy can't eat while playing
  def feed(self, puppy):
    return "The puppy is too busy playing with the ball to eat right now."

  def play(self, puppy):
    puppy.inc_plays()
    # If the puppy plays 2 or more times in a row, it falls asleep
    if puppy.plays > 1:
      #change state from playing to sleeping and reset plays and sleeps
      puppy.change_state(state_asleep.StateAsleep())
      puppy.reset()
      return "You throw the ball again and the puppy excitedly chases it.\nThe puppy played so much it fell asleep!"
    return "You throw the ball again and the puppy excitedly chases it."