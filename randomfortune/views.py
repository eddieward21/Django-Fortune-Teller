from django.shortcuts import render
import random
# Create your views here.
def fortune(request):
    fortune = random.choice(fortuneList)
    context = {
    'fortune': fortune
    }
    return render(request, 'randomfortune/fortune.html', context=context)



fortuneList = [
    "All will go well with your new project.",
   "If you continually give, you will continually have.",
   "Self-knowledge is a life long process.",
   "You are busy, but you are happy.",
   "Your abilities are unparalleled.",
   "Those who care will make the effort.",
   "Now is the time to try something new.",
   "Miles are covered one step at a time.",
   "Dont just think, act!",
   "There is nothing impossible to they who will try.",
   "Success is not final, failure is not fatal: it is the courage to continue that counts.",
   "What lies behind you and what lies in front of you, pales in comparison to what lies inside of you",
   "It is during our darkest moments that we must focus to see the light.",
   "All you need is the plan, the road map, and the courage to press on to your destination.",
   "Real change, enduring change, happens one step at a time.",
   "We generate fears while we sit. We overcome them by action.",
   "Out of the mountain of despair, a stone of hope.",
   "How wild it was, to let it be.",
   "The only journey is the one within.",
   "Fall seven times and stand up eight",
   "Failure is only the opportunity to begin again, this time more intelligently.",
   "What if I told you that 10 years from now, your life would be exactly the same? I doubt you'd be happy. So, why are you so afraid of change?",
   "Success is the sum of small efforts, repeated day in and day out.",
   " It does not matter how slowly you go so long as you do not stop.",
   "Never confuse a single defeat with a final defeat",
   "Success seems to be largely a matter of hanging on after others have let go.",
   "Failure is often that early morning hour of darkness which precedes the dawning of the day of success.",
   "It always seems impossible until it's done.",
   "Find a way or make one",
   "A winner is just a loser who tried one more time.",
   "Work and you’ll get what you need; work harder and you’ll get what you want.",
]


