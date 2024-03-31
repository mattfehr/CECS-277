import puppystate
import state_asleep
import state_play

class StateEat(puppystate.PuppyState):
  def play(self, puppy):
    puppy.change_state(state_play.StatePlay())
    puppy.reset()
    return "The puppy looks up from its food and chases the ball you threw."

  def feed(self, puppy):
    puppy.inc_feeds()
    # If the puppy eats 2 or more scoops in a row, it falls asleep
    if puppy.feeds > 1:
      #change state from eating to sleeping and reset plays and feeds
      puppy.change_state(state_asleep.StateAsleep())
      puppy.reset()
      return "The puppy continues to eat as you add another scoop of kibble to its bowl.\nThe puppy ate so much it fell asleep!"
    return "The puppy continues to eat as you add another scoop of kibble to its bowl."

