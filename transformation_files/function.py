import azure.functions as func
import logging
import pandas as pd
from transformation_files.merge_files import merge_csv_files

def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    try:
        merged_file_path = merge_csv_files()
        merged_df = pd.read_csv(merged_file_path)
        merged_json = merged_df.to_json(orient="records")

        return func.HttpResponse(merged_json, mimetype="application/json", status_code=200)

    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
