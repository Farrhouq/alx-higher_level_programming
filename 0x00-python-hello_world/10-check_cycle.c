#include "lists.h"

/**
 * check_cycle - checks if a list has a loop
 * @list: the listint to check
 * Return: 0 if there is no loop, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	if (list == NULL)
		return (0);
	hare = list;
	tortoise = list;
	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}

	return (0);
}
