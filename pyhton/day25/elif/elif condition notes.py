''' ELSE IF CONDITON:
      1.when we have multiple conditions we can use elif block.

     2.in elif condiotion we can use else block but else block is optional.

     3.in elif condition we can use multiple elif block based on the condition.


  SYNTAX:---->if condition:             ------->TSB
                                 statement

                          elif condition:           ------->TSB
                                statement
                                
                        elif condition:             ------->TSB
                                statement
                                
                        elif condition:               ------->TSB
                                statement
                                
                        elif condition:             ------->TSB
                                statement

                        else:                          ------->FSB(optional)
                            condition








FLOWCHART:


                                                       [   START   ]
                                                                |
                                                                |
                                                    [  Condition 1   ]
                                                                |
                                                                |
                              -----------------------------------------------------
                              |                                                                      |
                        [ TRUE ]                                                         [  FALSE  ]
                              |                                                                     |
        [  Block will  execute   ]                                                 [ condition2 ]
                                                                                                    |
                                                                            -----------------------------------------
                                                                            |                                                      |
                                                                     [ TRUE  ]                                         [  FALSE ]
                                                                            |                                                       |
                                                          [  Block will execute   ]                              [ Condition 3 ]
                                                                                                                                    |
                                                                                                                  -----------------------------
                                                                                                                  |                                     |
                                                                                                          [  TRUE   ]                    [   FALSE  ]
                                                                                                                 |                                      |
                                                                                             [  Block will execute  ]               [  Blank space ]
