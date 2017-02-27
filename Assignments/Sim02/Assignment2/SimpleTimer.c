// Program Information ////////////////////////////////////////////////////////
/**
 * @file SimpleTimer.c
 *
 * @brief Implementation file for using a timer with micro-second precision
 *
 * @author Michael Leverington
 *
 * @details Implements member methods for timing
 *
 * @version 2.00 (13 January 2017)
 *          1.00 (11 September 2015)
 *
 * @Note Requires SimpleTimer.h.
 *
 */

// Precompiler directives /////////////////////////////////////////////////////

#ifndef SIMPLETIMER_CPP
#define SIMPLETIMER_CPP


// Header files ///////////////////////////////////////////////////////////////

#include "SimpleTimer.h"

double accessTimer( int controlCode, char *timeStr)
   {
    static Boolean running = False;
    static Boolean dataGood = False;
    static int startSec = 0, endSec = 0, startUSec = 0, endUSec = 0;
    struct timeval startData, endData;
    double fpTime = 0.0;
    int secDiff, usecDiff;

    switch( controlCode )
       {
        case START_TIMER:
           gettimeofday( &startData, NULL );
           running = True;
           dataGood = False;

           startSec = startData.tv_sec;
           startUSec = startData.tv_usec;
           fpTime = (double) startSec + (double) startUSec / 1000000;
           break;

        case STOP_TIMER:
           if( running == True )
              {
               gettimeofday( &endData, NULL );
               running = False;
               dataGood = True;
               endSec = endData.tv_sec;
               endUSec = endData.tv_usec;
               fpTime = (double) endSec + (double) endUSec / 1000000;
              }

           // assume timer not running
           else
              {
               dataGood = False;
               fpTime = 0.0;
              }

           break;

        case RESET_TIMER:
           running = False;
           dataGood = False;
           startSec = 0;
           endSec = 0;
           startUSec = 0;
           endUSec = 0;
           fpTime = 0.0;
           break;

        case GET_TIME_DIFF:
           if( running == False && dataGood == True )
              {
               secDiff = endSec - startSec;
               usecDiff = endUSec - startUSec;
               fpTime = (double) secDiff + (double) usecDiff / 1000000;
               if( usecDiff < 0 )
                  {
                   usecDiff = usecDiff + 1000000;
                   secDiff = secDiff - 1;
                  }

               timeToString( secDiff, usecDiff, timeStr );
              }

           // assume timer running or data not good
           else
              {
               fpTime = 0.0;
              }

           break;
       }

    return fpTime;
   }

/* This is a bit of a drawn-out function, but it is written
   to force the time result to always be in the form x.xxxxxxx
   when printed as a string; this will not always be the case
   when the time is presented as a floating point number
*/
void timeToString( int secTime, int uSecTime, char *timeStr )
   {
    int low, high, index = 0;
    char temp;

    while( uSecTime > 0 )
       {
        timeStr[ index ] = (char) uSecTime % 10 + '0';
         uSecTime /= 10;

        index++;
       }

    while( index < 6 )
       {
        timeStr[ index ] = '0';

        index++;
       }

    timeStr[ index ] = RADIX_POINT;

    index++;

    if( secTime == 0 )
       {
        timeStr[ index ] = '0';

        index++;
       }

    while( secTime > 0 )
       {
        timeStr[ index ] = (char) secTime % 10 + '0';

        secTime /= 10;

        index++;
       }

    timeStr[ index ] = NULL_CHAR;

    low = 0; high = index - 1;

    while( low < high )
       {
        temp = timeStr[ low ];
        timeStr[ low ] = timeStr[ high ];
        timeStr[ high ] = temp;

        low++; high--;
       }
   }

#endif // ifndef SIMPLETIMER_CPP
