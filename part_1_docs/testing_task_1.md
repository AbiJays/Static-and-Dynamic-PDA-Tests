### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      # need == meaning 'is equal to' not the assigning '=' operand
      return True
    else
    # else needs a semicolon after it.
      return False
   

  dif highest_card(self, card1 card2): 
    # def spelled incorrectly
    # no comma separating the two parameters 
  if card1.value > card2.value:
    # needs to be indented one to the right so it is contained within the highest_card() method
    return card 
    # "card" is not defined, presumably they mean card1?
  else:
    return card2
  


def cards_total(self, cards):
  total
  # total means nothing, it has not been assigned anything so is not a usable variable. 
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # identation of return statement is incorrect. Needs to be at the same level at for in order to get total, otherwise it will iterate evey loop.
```
