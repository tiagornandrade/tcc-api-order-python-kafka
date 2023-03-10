from psycopg2.extras import DictCursor
from database.dbConnect import connectionTransaction


connection = connectionTransaction()


def transactionGetItem():
    with connection:
        with connection.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute("""SELECT * FROM public.transaction_created;""")
            transaction_get_itens = cursor.fetchall()
            cursor.close()
            response_itens = [row_to_dict_transaction(x) for x in transaction_get_itens]
    return response_itens


def row_to_dict_transaction(row):
    return dict(
        {"transaction_id": row["transaction_id"], "transaction": row["transaction"]}
    )
