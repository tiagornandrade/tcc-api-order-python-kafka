from dbConnect import connectionRead


connection = connectionRead()

CREATE_ORDER_TABLE = """
    CREATE table if not EXISTS public.order (
        id TEXT,
        name TEXT,
        description TEXT,
        price FLOAT
    );
"""

CREATE_TRANSACTION_TABLE = """
    CREATE table if not EXISTS public.transaction (
        transaction_id TEXT,
        transaction json
    );
"""

with connection:
    with connection.cursor() as cursor:
        cursor.execute(CREATE_ORDER_TABLE)
        cursor.execute(CREATE_TRANSACTION_TABLE)
