#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - sleeps infinitely
 *
 * Return: returns 0 on completion
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 *
 * Return: returns 0 on successful completion
 */
int main(void)
{
	int count = 0;
	pid_t child;

	while (count < 5)
	{
		child = fork();
		if (child > 0)
			printf("Zombie process created, PID: %d\n", child);
		else
			exit(0);
		count++;
	}
	infinite_while();

	return (0);
}
