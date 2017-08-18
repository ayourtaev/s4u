# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Account(models.Model):
    """
    class description
    """
    CURRENCY_CHOICES = (
            ('USD', 'USD'),
            ('EUR', 'EUR'),
            ('GBR', 'GBR'),
            ('CHF', 'CHF'),
    )

    id = models.AutoField(
        primary_key=True
    )

    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES, default='USD')
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return "{:08d}".format(self.id)


class Transaction(models.Model):
    """
    Transaction
    """
    source = models.ForeignKey('Account', related_name='source', blank=True, null=True)
    destination = models.ForeignKey('Account', related_name='destination')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
