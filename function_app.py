# import azure.functions as func
# import logging
# import os
# import pandas as pd
# from merge.merge_files import merge_csv_files

# app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# @app.route(route="http_trigger")
# def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info("Python HTTP trigger function processed a request.")

#     try:
#         merged_file_path = merge_csv_files()
#         merged_df = pd.read_csv(merged_file_path)
#         merged_json = merged_df.to_json(orient="records")

#         return func.HttpResponse(merged_json, mimetype="application/json", status_code=200)

#     except Exception as e:
#         logging.error(f"Error processing request: {e}")
#         return func.HttpResponse(f"Error: {str(e)}", status_code=500)

import azure.functions as func
from transformation_files.function import http_trigger

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="mdm/merge/http_trigger")
def run_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    return http_trigger(req)

