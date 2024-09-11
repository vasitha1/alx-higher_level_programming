#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - Function that inserts a value in the right other in a sorted linked list
 * @head: Pointer to the next node
 * @number: The value of the data part of node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *node;

	temp = NULL;
	node = malloc(sizeof(listint_t));

	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}

	temp = *head;
	while (temp->next != NULL && temp->next->n < number)
	{
		temp = temp->next;
	}
	node->next = temp->next;
	temp->next = node;
	return(node);
}
