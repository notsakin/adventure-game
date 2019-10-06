print('             Gebe nun deinen Namen ein. Er darf maximal 10 Zeichen lang sein.')
playername = input('             >> ')
while playername == len(playername) >= 10:
    textbox('Professor E.', 'Huch, dein Name scheint', ' zu lang zu sein.', '')
    newScreen()
    textbox('Professor E.', 'Huch, dein Name scheint', ' zu lang zu sein.', 'Probiers nochmal.')
    awatingInput()
    print('             Gebe nun deinen Namen ein. Er darf maximal 10 Zeichen lang sein.')
    playername = input('             >> ')


#playernameConfirm
newScreen()
print('             ', playername,' wird nun dein Name sein. Fortfahren? \n\n              [Ja / Name ändern] \n\n\n\n')
playernameConfirm = input('             >> ')
if playernameConfirm == str('Ja'):


if playernameConfirm == str('Name ändern'):
    newScreen()
    textbox('Professor E.', 'Na, wie heißt du denn jetzt?', '', '')
    time.sleep(2)
    print('             Gebe nun deinen Namen ein. Er darf maximal 10 Zeichen lang sein.')
    playername = input('             >> ')
    newScreen()
    print('             ', playername,' wird nun dein Name sein. Fortfahren? \n\n              [Ja / Name ändern] \n\n\n\n')
    playernameConfirm = input('             >>')

if playernameConfirm != arr['Ja', 'Name ändern']:
    print('')

newScreen()
