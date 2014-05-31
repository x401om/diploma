//
//  main.c
//  Core_xcode
//
//  Created by Aleksey Goncharov on 31.05.14.
//  Copyright (c) 2014 x401om. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>

#include "C:\Users\Gala Boldyreva\Documents\GitHub\diploma\Core_files\game.h"

// some constants for game initializaton
#define kStabilityAmount (int)3
#define kNumberOfPlayers (int)3

int main(int argc, const char * argv[]) {
  double resource = 1000.0;
  
  Player *players = (Player *)malloc(kNumberOfPlayers*sizeof(Player));
  int step = 0;
  while (1) {
    step++;
    printf("step number %d\n", step);
    for (int i = 0; i < kNumberOfPlayers; ++i) {
      printf("enter the demand of player #%d\n", i+1);
      scanf_s("%lf", &(players[i].demand));
    }
    for (int i = 0; i < kNumberOfPlayers; ++i) {
      calculateMetrics(players, resource);
      printf("player #\tdemand\tprofit\tutility\n");
      printf("%d\t%.2lf\t%.2lf\t%.2lf\n\n", i+1, players[i].demand, players[i].profit, players[i].utility);
    }

  }
  
  return 0;
}

