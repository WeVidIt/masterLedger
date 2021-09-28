"""testingsite3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from hordak import views as hordak_views
from hordak.views import accounts, statement_csv_import
from hordak.views import transactions
from django.urls.base import reverse_lazy

hordak_urls = [
    url(
        r"^transactions/create/$",
        transactions.TransactionCreateView.as_view(),
        name="transactions_create",
    ),
    url(
        r"^transactions/(?P<uuid>.+)/delete/$",
        transactions.TransactionDeleteView.as_view(),
        name="transactions_delete",
    ),
    url(
        r"^transactions/currency/$", transactions.CurrencyTradeView.as_view(), name="currency_trade"
    ),
    url(
        r"^transactions/reconcile/$",
        transactions.TransactionsReconcileView.as_view(),
        name="transactions_reconcile",
    ),
    url(
        r"^transactions/list/$",
        transactions.TransactionsListView.as_view(),
        name="transactions_list",
    ),
    url(r"^transactions/legs/$", transactions.LegsListView.as_view(), name="legs_list"),
    url(
        r"^statement-line/(?P<uuid>.+)/unreconcile/$",
        transactions.UnreconcileView.as_view(),
        name="transactions_unreconcile",
    ),
    url(r"^$", accounts.AccountListView.as_view(), name="accounts_list"),
    url(r"^accounts/create/$", accounts.AccountCreateView.as_view(), name="accounts_create"),
    url(
        r"^accounts/update/(?P<uuid>.+)/$",
        accounts.AccountUpdateView.as_view(),
        name="accounts_update",
    ),
    url(
        r"^accounts/(?P<uuid>.+)/$",
        accounts.AccountTransactionsView.as_view(),
        name="accounts_transactions",
    ),
    url(r"^import/$", statement_csv_import.CreateImportView.as_view(), name="import_create"),
    url(
        r"^import/(?P<uuid>.*)/setup/$",
        statement_csv_import.SetupImportView.as_view(),
        name="import_setup",
    ),
    url(
        r"^import/(?P<uuid>.*)/dry-run/$",
        statement_csv_import.DryRunImportView.as_view(),
        name="import_dry_run",
    ),
    url(
        r"^import/(?P<uuid>.*)/run/$",
        statement_csv_import.ExecuteImportView.as_view(),
        name="import_execute",
    ),
]

urlpatterns = [
    path('appTestingHordak/', include('appTestingHordak.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('hordak.urls', namespace='hordak')),
    url(r'^accounts/$', hordak_views.AccountListView.as_view(), name='accounts_list'),
    url(r'^accounts/create/$', hordak_views.AccountCreateView.as_view(success_url=reverse_lazy('accounts_list')), name='accounts_create'),
]
