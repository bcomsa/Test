
#include "Util.h"
#include <iostream>
#include "time.h"
 
using namespace std;
 
struct Pos2D {
    int x; int y;
    int ox; int oy;
};
int boardW, boardH;
Pos2D snake[100]; int snakeLength;
Pos2D direction;
bool endGame;
// �o^` �n ��y
Pos2D food;
int tickSpeed;
 
void init() {
    // kho+?i ta.o mo^.t so^' gi� tri. ban �a^`u
    endGame = false;
    tickSpeed = 70;
    boardW = 50; boardH = 20;
    // kho+?i ta.o con ra('n go^`m c� 2 �
    snake[0].x = 5; snake[0].y = 5;
    snake[1].x = 4; snake[1].y = 5;
    snakeLength = 2;
    // h�o+'ng di chuye^?n ban �a^`u l� �i xuo^'ng
    direction.x = 0; direction.y = 1;
    // �a(.t m�u ne^`n cho m�n hi`nh
    SetBGColor(8);
    for (int i = 0; i < boardW; i++) {
        for (int j = 0; j < boardH; j++) {
            gotoxy(i, j);
            printf(" ");
        }
    }
    // �a(.t m�u chu+~
    SetColor(14);
    // vi. tr� ban �a^`u cho food
    food.x = 25; food.y = 10;
}
 
void moveSnake(Pos2D dir) {
    for (int i = 0; i < snakeLength; i++) {
        if (i == 0) {
            // di chuye^?n �a^`u ra('n
            snake[0].ox = snake[0].x; snake[0].oy = snake[0].y;
            snake[0].x += dir.x; snake[0].y += dir.y;
        }else{
            // di chuye^?n pha^`n th�n ra('n
            snake[i].ox = snake[i].x; snake[i].oy = snake[i].y;
            snake[i].x = snake[i - 1].ox; snake[i].y = snake[i - 1].oy;
        }
        // kie^?m tra coi con ra('n c� ca('n tr�ng n� kh�ng
        if (i != 0 && (snake[0].x == snake[i].x && snake[0].y == snake[i].y)) endGame = true;
    }
 
    // khi ra('n v�o+.t ra kho?i m�n hi`nh thi` cho n� xua^'t hie^.n la.i
    if (snake[0].x >= boardW) snake[0].x = 0;
    if (snake[0].x < 0) snake[0].x = boardW - 1;
    if (snake[0].y >= boardH) snake[0].y = 0;
    if (snake[0].y < 0) snake[0].y = boardH - 1;
 
    // kie^?m tra coi con ra('n c� �n tr�ng food ch�a
    if (snake[0].x == food.x && snake[0].y == food.y) {
        snake[snakeLength].x = snake[snakeLength - 1].ox; snake[snakeLength].y = snake[snakeLength - 1].oy;
        snakeLength++;
        srand ( time(NULL) );
        food.x = rand() % boardW;
        food.y = rand() % boardH;
        if (tickSpeed > 5)
            tickSpeed -= 5;
    }
}
 
void drawFood() {
    // do.n �o^` �n ra n�o
    SetColor(12);
    gotoxy(food.x, food.y);
    printf("%c", 2);
}
 
void drawSnake() {
    SetColor(14);
    for (int i = 0; i < snakeLength; i++) {
        gotoxy(snake[i].x, snake[i].y);
        printf("%c", 4); // d�ng k� tu+. hi`nh kim c��ng �e^? ve~ con ra('n
    }
    gotoxy(snake[snakeLength-1].ox, snake[snakeLength-1].oy);
	printf(" "); // x�a pha^`n �u�i tr�o+'c �� cu?a n�
}
 
void mainloop() {
    moveSnake(direction);
 
    if (checkKey(KEY_LEFT)) {
        if (direction.x != 1) {
            direction.x = -1; direction.y = 0;
        }
    }
    else if (checkKey(KEY_RIGHT)) {
        if (direction.x != -1) {
            direction.x = 1; direction.y = 0;
        }
    }
    else if (checkKey(KEY_UP)) {
        if (direction.y != 1) {
            direction.y = -1; direction.x = 0;
        }
    }
    else if (checkKey(KEY_DOWN)) {
        if (direction.y != -1) {
            direction.y = 1; direction.x = 0;
        }
    }
 
    if (checkKey(KEY_ESC)) {
        endGame = true;
    }
}
 
void drawgame() {
    drawFood();
    drawSnake();
     
    SetColor(10);
    gotoxy(0, 0);
    printf("Diem: %d", snakeLength*100);
}
 
int main() {
    init();
    ShowCur(false); // A^?n con tro?
    while (!endGame){
        Tick(tickSpeed, mainloop, drawgame); // Mainloop
    }
    return 0;
}
