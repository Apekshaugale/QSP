'''
NESTED IF STSTEMENT:
              A if statement inside another if  statement is  known as nested if statement.


SYNTAX: if condition1:
                        if condition2:
                                if condition3:
                                else:
                                    FSB3
                        else:
                            FSB2
                 else:
                   FSB1



Work Flow:
                                            START
                                                  |
                                    [  if condition1    ]------------False----[ else FSB 1]
                                                  |
                                             True
                                                  |
                                   [   if condition2  ]--------False----[ else: FSB2 ]
                                                  |
                                            True
                                                 |
                                  [   if condition3  ]--------False----[ else: FSB3 ]
                                                                                                |
                                                                                                |
                                                                                        [ STOP ]
