//
//  game.c
//  Core_xcode
//
//  Created by Aleksey Goncharov on 31.05.14.
//  Copyright (c) 2014 x401om. All rights reserved.
//

#include <stdio.h>
#include "game.h"

double calculateProfitForUser(int playerIndex, Player *players, double resource) {
  Player player = players[playerIndex];
  double profit = 0.0;
  int numberOfPlayers = 3;//sizeof(players)/sizeof(Player);
  for (int i = 0; i < numberOfPlayers; ++i) {
    profit += resource*(player.demand - players[i].demand)/numberOfPlayers;
  }
  return profit;
}

double calculateUtilityForPlayer(Player player, double resource) {
  double utility = (resource - player.profit)/resource;
  return utility;
}

void calculateMetrics(Player *players, double resource) {
  int numberOfPlayers = 3;//sizeof(players)/sizeof(Player);
  for (int i = 0; i < numberOfPlayers; ++i) {
    players[i].profit = calculateProfitForUser(i, players, resource);
    players[i].utility = calculateUtilityForPlayer(players[i], resource);
  }
}