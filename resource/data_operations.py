import pandas as pd
import logging
from flask_restful import Resource
from common.config import db_connection

class DataTypeConversion(Resource):
    def post(self):
        connection = None
        try:
            logging.info("Datatype conversion API started")

            logging.info("Establishing database connection")
            connection = db_connection()

            if connection is None:
                return {"res_status": False, "msg": "Database connection failed"}

            query = """
                    SELECT *
                    FROM data_auth
                    """

            logging.info("Reading data from data_auth table")
            df = pd.read_sql(query, connection)

            logging.info(f"Total records fetched: {len(df)}")

            schema_query = """
                            SELECT
                                column_name,
                                data_type
                            FROM information_schema.columns
                            WHERE table_name = 'data_auth'
                            """

            logging.info("Fetching schema information")
            schema_df = pd.read_sql(schema_query, connection)

            logging.info("Original SQL schema fetched successfully")

            print("Original SQL Schema:")
            print(schema_df.to_string(index=False))

            string_columns = schema_df[
                schema_df["data_type"].isin([
                    "character varying",
                    "text",
                    "varchar",
                    "uuid",
                    "jsonb"
                ])
            ]["column_name"]

            logging.info(f"String columns identified: {list(string_columns)}")

            date_columns = schema_df[
                schema_df["data_type"].isin([
                    "timestamp without time zone",
                    "timestamp with time zone",
                    "date"
                ])
            ]["column_name"]

            logging.info(f"Date columns identified: {list(date_columns)}")

            numeric_columns = schema_df[
                schema_df["data_type"].isin([
                    "integer",
                    "bigint",
                    "smallint",
                    "numeric",
                    "decimal"
                ])
            ]["column_name"]

            logging.info(f"Numeric columns identified: {list(numeric_columns)}")

            logging.info("Converting string columns")
            df[string_columns] = df[string_columns].astype("string")

            logging.info("Converting date columns")
            df[date_columns] = df[date_columns].apply(pd.to_datetime)

            logging.info("Converting numeric columns")
            df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)

            logging.info("Datatype conversion completed successfully")

            print("Converted DataTypes:\n", df.dtypes)

            logging.info(f"Final DataTypes:\n{df.dtypes}")

            return {"message": "Datatype conversion completed successfully"}

        except Exception as e:
            logging.error(f"Error occurred: {str(e)}")

            return {"error": str(e)}

        finally:
            if connection:
                connection.close()
                logging.info("Database connection closed")