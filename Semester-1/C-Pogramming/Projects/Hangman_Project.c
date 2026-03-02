#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>

#define MAX_WRONG 6
#define MAX_WORD_LEN 32

const char *WORDS[] = {
    "code", "hangman", "array", "pointer", "variable",
    "function", "loop", "binary", "compile", "string"
};
const int WORD_COUNT = sizeof(WORDS) / sizeof(WORDS[0]);

const char* choose_word() {
    return WORDS[rand() % WORD_COUNT];
}

void make_mask(const char *word, char mask[]) {
    int n = (int)strlen(word);
    for (int i = 0; i < n; i++) mask[i] = '_';
    mask[n] = '\0';
}

int used_before(char g, const char *mask, const char *wrong) {
    for (int i = 0; mask[i]; i++) if (tolower((unsigned char)mask[i]) == g) return 1;
    for (int i = 0; wrong[i]; i++) if (wrong[i] == g) return 1;
    return 0;
}

int apply_guess(const char *word, char mask[], char g) {
    int hits = 0;
    for (int i = 0; word[i]; i++) {
        if (tolower((unsigned char)word[i]) == g && mask[i] == '_') {
            mask[i] = word[i];
            hits++;
        }
    }
    return hits;
}

int main() {
    srand((unsigned)time(NULL));
    const char *secret = choose_word();
    char mask[MAX_WORD_LEN];
    char wrong[27] = "";
    int wrong_count = 0;

    make_mask(secret, mask);

    printf("=== Hangman (Simple) ===\n");
    printf("The word has %d letters.\n\n", (int)strlen(secret));

    while (1) {

        printf("Word: ");
        for (int i = 0; mask[i]; i++) printf("%c ", mask[i]);
        printf("\nWrong letters: %s\n", wrong);
        printf("Chances left: %d\n", MAX_WRONG - wrong_count);


        if (strcmp(secret, mask) == 0) {
            printf("\nYou WIN! The word was: %s\n", secret);
            break;
        }
        if (wrong_count >= MAX_WRONG) {
            printf("\nYou LOSE! The word was: %s\n", secret);
            break;
        }


        printf("Enter a letter: ");
        char input;
        if (scanf(" %c", &input) != 1) { 
            printf("\nInput error. Exiting.\n");
            break;
        }

        char g = (char)tolower((unsigned char)input);

        if (!isalpha((unsigned char)g)) {
            printf("Please enter letters only.\n\n");
            continue;
        }

        if (used_before(g, mask, wrong)) {
            printf("You already tried '%c'.\n\n", g);
            continue;
        }

        int hits = apply_guess(secret, mask, g);
        if (hits > 0) {
            printf("Nice! '%c' occurs %d time(s).\n\n", g, hits);
        } else {
            int len = (int)strlen(wrong);
            wrong[len] = g;
            wrong[len + 1] = '\0';
            wrong_count++;
            printf("Nope! '%c' is not in the word.\n\n", g);
        }
    }
    return 0;

}
