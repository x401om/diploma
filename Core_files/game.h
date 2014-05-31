//
//  game.h
//  Core_xcode
//
//  Created by Aleksey Goncharov on 31.05.14.
//  Copyright (c) 2014 x401om. All rights reserved.
//

#ifndef Core_xcode_game_h
#define Core_xcode_game_h



typedef struct {
  double demand; // запрос
  double profit; // получил
  double utility; // полезность
} Player;

/**
 *  method calculates profit value for existing player
 *  based on another players' demands
 *
 *  @param playerIndex the index of player which profit you want to calculate
 *  @param players   the array of players taking part in the game
 *  @param resource  amount of global resource
 *
 *  @return value of profit for giving player
 */
double calculateProfitForUser(int playerIndex, Player *players, double resource);

/**
 *  method calculates utility value fot giving player
 *
 *  @param player struct for calculating
 *
 *  @return calculated utility value
 */
double calculateUtilityForPlayer(Player player, double resource);

/**
 *  calculates all the metrics for current step
 *
 *  @param players
 *  @param resouse
 */
void calculateMetrics(Player *players, double resource);

#endif
