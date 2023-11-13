import re;

nameSchedules = [];
timeSchedules = [];
hairStyle = [];

def printSeparate():
    print('=================================================');

def isTimeValid(userTimeInput):
    timePattern = r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$'

    if re.match(timePattern, userTimeInput):
        return True;
    else:
        return False;

def removeScheduling():
    if not nameSchedules:
        printSeparate();
        print('A lista está vazia!');
        printSeparate();
        return;

    seeScheduling();

    loop = True;

    while loop != False:
        print('Para cancelar, digite 0!');
        removeIndex = int(input('Qual horário você deseja remover? '));

        if removeIndex == 0:
            printSeparate();
            return;
        elif removeIndex:
            if removeIndex < 1 or removeIndex > len(nameSchedules):
                print('O horário digitado não está na lista!');
            else:
                printSeparate();
                print('Horário removido com sucesso!');
                printSeparate();
                removeIndex -= 1;
                del nameSchedules[removeIndex];
                del timeSchedules[removeIndex];
                del hairStyle[removeIndex];
                return;
        else:
            print('O campo é obrigatório!')
    
def addScheduling():
    loop = True;

    while loop != False:
        printSeparate();
        print('Para cancelar, digite cancelar em qualquer campo!')
        personNameInput = input('Digite o nome do cliente: ');
        
        if personNameInput:

            if(personNameInput == 'cancelar'):
                printSeparate();
                break;

            timeInput = input('Digite o horário (formato 24 horas (00:00 - 23:59)): ');

            if timeInput:

                if(timeInput == 'cancelar'):
                    printSeparate();
                    break;
                elif(not isTimeValid(timeInput)):
                    printSeparate();
                    print('Formato de horário inválido, deve estar entre 00:00 e 23:59, e caso seja menor que 10, deve possuir um 0 na frente (09:09)!');
                    continue;

                hairStyleInput = input('Digite o tipo do corte (opicional): ');

                if(hairStyleInput == 'cancelar'):
                    printSeparate();
                    break;
                elif(hairStyleInput == ''):
                    hairStyleInput = '?';

                printSeparate();
                print('Horário adicionado com sucesso!');
                printSeparate();
                nameSchedules.append(personNameInput);
                timeSchedules.append(timeInput);
                hairStyle.append(hairStyleInput);
                return;
            else:
                printSeparate();
                print('O horário é obrigatório!');
        else:
            printSeparate();
            print('O nome é obrigatório!');
                    
def seeScheduling():
    if not nameSchedules:
        printSeparate();
        print('A lista está vazia!');
        printSeparate();
        return;

    loop = True;
    index = 0;

    printSeparate();

    while loop != False:
        print('[{}] Nome: {}; Horário: {}; Tipo de corte: {};'.format(index + 1, nameSchedules[index], timeSchedules[index], hairStyle[index]));
        index = index + 1;
        
        if index == len(nameSchedules):
            printSeparate();
            return;

def chooseAction():
    loop = True;
    while loop != False: 
        choice = int(input('[1] Adicionar horário \n[2] Remover horário \n[3] Ver horários \n[4] Fechar programa \nEscolha: '));
        
        if(choice == 1):
            addScheduling();
        elif(choice == 2):
            removeScheduling();
        elif(choice == 3):
            seeScheduling();
        elif(choice == 4):
            printSeparate();
            print('Volte sempre :)');
            printSeparate();
            return;
        else:
            printSeparate();
            print('Opção inválida!');
            printSeparate();

if __name__ == '__main__':
    chooseAction();
