{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a62124b5",
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "source": [
    "XÂY DỰNG DATA PIPELINE LOAD DỮ LIỆU LÊN BIGQUERY"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f171cb9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in d:\\anaconda\\lib\\site-packages (2.3.3)\n",
      "Requirement already satisfied: numpy>=1.26.0 in d:\\anaconda\\lib\\site-packages (from pandas) (2.3.5)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in d:\\anaconda\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in d:\\anaconda\\lib\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in d:\\anaconda\\lib\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: six>=1.5 in d:\\anaconda\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
      "Collecting google-cloud-bigquery\n",
      "  Downloading google_cloud_bigquery-3.42.1-py3-none-any.whl.metadata (8.0 kB)\n",
      "Collecting pandas-gbq\n",
      "  Downloading pandas_gbq-0.35.0-py3-none-any.whl.metadata (3.7 kB)\n",
      "Collecting google-api-core<3.0.0,>=2.11.1 (from google-api-core[grpc]<3.0.0,>=2.11.1->google-cloud-bigquery)\n",
      "  Downloading google_api_core-2.31.0-py3-none-any.whl.metadata (3.2 kB)\n",
      "Collecting google-auth<3.0.0,>=2.14.1 (from google-auth[pyopenssl]<3.0.0,>=2.14.1->google-cloud-bigquery)\n",
      "  Downloading google_auth-2.55.1-py3-none-any.whl.metadata (5.1 kB)\n",
      "Collecting google-cloud-core<3.0.0,>=2.4.1 (from google-cloud-bigquery)\n",
      "  Downloading google_cloud_core-2.6.0-py3-none-any.whl.metadata (2.8 kB)\n",
      "Collecting google-resumable-media<3.0.0,>=2.0.0 (from google-cloud-bigquery)\n",
      "  Downloading google_resumable_media-2.10.0-py3-none-any.whl.metadata (2.2 kB)\n",
      "Requirement already satisfied: packaging>=24.2.0 in d:\\anaconda\\lib\\site-packages (from google-cloud-bigquery) (25.0)\n",
      "Requirement already satisfied: python-dateutil<3.0.0,>=2.8.2 in d:\\anaconda\\lib\\site-packages (from google-cloud-bigquery) (2.9.0.post0)\n",
      "Requirement already satisfied: requests<3.0.0,>=2.21.0 in d:\\anaconda\\lib\\site-packages (from google-cloud-bigquery) (2.32.5)\n",
      "Collecting googleapis-common-protos<2.0.0,>=1.63.2 (from google-api-core<3.0.0,>=2.11.1->google-api-core[grpc]<3.0.0,>=2.11.1->google-cloud-bigquery)\n",
      "  Downloading googleapis_common_protos-1.75.0-py3-none-any.whl.metadata (8.6 kB)\n",
      "Collecting protobuf<8.0.0,>=5.29.6 (from google-api-core<3.0.0,>=2.11.1->google-api-core[grpc]<3.0.0,>=2.11.1->google-cloud-bigquery)\n",
      "  Downloading protobuf-7.35.1-cp310-abi3-win_amd64.whl.metadata (595 bytes)\n",
      "Collecting proto-plus<2.0.0,>=1.24.0 (from google-api-core<3.0.0,>=2.11.1->google-api-core[grpc]<3.0.0,>=2.11.1->google-cloud-bigquery)\n",
      "  Downloading proto_plus-1.28.0-py3-none-any.whl.metadata (2.2 kB)\n",
      "Collecting requests<3.0.0,>=2.21.0 (from google-cloud-bigquery)\n",
      "  Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)\n",
      "Collecting grpcio<2.0.0,>=1.41.0 (from google-api-core[grpc]<3.0.0,>=2.11.1->google-cloud-bigquery)\n",
      "  Downloading grpcio-1.81.1-cp313-cp313-win_amd64.whl.metadata (3.8 kB)\n",
      "Collecting grpcio-status<2.0.0,>=1.41.0 (from google-api-core[grpc]<3.0.0,>=2.11.1->google-cloud-bigquery)\n",
      "  Downloading grpcio_status-1.81.1-py3-none-any.whl.metadata (1.2 kB)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in d:\\anaconda\\lib\\site-packages (from google-auth<3.0.0,>=2.14.1->google-auth[pyopenssl]<3.0.0,>=2.14.1->google-cloud-bigquery) (0.4.2)\n",
      "Requirement already satisfied: cryptography>=38.0.3 in d:\\anaconda\\lib\\site-packages (from google-auth<3.0.0,>=2.14.1->google-auth[pyopenssl]<3.0.0,>=2.14.1->google-cloud-bigquery) (46.0.3)\n",
      "Requirement already satisfied: pyopenssl>=20.0.0 in d:\\anaconda\\lib\\site-packages (from google-auth[pyopenssl]<3.0.0,>=2.14.1->google-cloud-bigquery) (25.3.0)\n",
      "Collecting google-crc32c<2.0.0,>=1.0.0 (from google-resumable-media<3.0.0,>=2.0.0->google-cloud-bigquery)\n",
      "  Downloading google_crc32c-1.8.0-cp313-cp313-win_amd64.whl.metadata (1.8 kB)\n",
      "Requirement already satisfied: typing-extensions~=4.12 in d:\\anaconda\\lib\\site-packages (from grpcio<2.0.0,>=1.41.0->google-api-core[grpc]<3.0.0,>=2.11.1->google-cloud-bigquery) (4.15.0)\n",
      "Requirement already satisfied: six>=1.5 in d:\\anaconda\\lib\\site-packages (from python-dateutil<3.0.0,>=2.8.2->google-cloud-bigquery) (1.17.0)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in d:\\anaconda\\lib\\site-packages (from requests<3.0.0,>=2.21.0->google-cloud-bigquery) (3.4.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in d:\\anaconda\\lib\\site-packages (from requests<3.0.0,>=2.21.0->google-cloud-bigquery) (3.11)\n",
      "Requirement already satisfied: urllib3<3,>=1.26 in d:\\anaconda\\lib\\site-packages (from requests<3.0.0,>=2.21.0->google-cloud-bigquery) (2.5.0)\n",
      "Requirement already satisfied: certifi>=2023.5.7 in d:\\anaconda\\lib\\site-packages (from requests<3.0.0,>=2.21.0->google-cloud-bigquery) (2025.11.12)\n",
      "Requirement already satisfied: setuptools in d:\\anaconda\\lib\\site-packages (from pandas-gbq) (80.9.0)\n",
      "Collecting db-dtypes<2.0.0,>=1.1.1 (from pandas-gbq)\n",
      "  Downloading db_dtypes-1.7.0-py3-none-any.whl.metadata (3.3 kB)\n",
      "Requirement already satisfied: numpy>=1.26.4 in d:\\anaconda\\lib\\site-packages (from pandas-gbq) (2.3.5)\n",
      "Requirement already satisfied: pandas>=1.5.3 in d:\\anaconda\\lib\\site-packages (from pandas-gbq) (2.3.3)\n",
      "Requirement already satisfied: pyarrow>=12.0.0 in d:\\anaconda\\lib\\site-packages (from pandas-gbq) (21.0.0)\n",
      "Collecting pydata-google-auth>=1.5.0 (from pandas-gbq)\n",
      "  Downloading pydata_google_auth-1.9.1-py2.py3-none-any.whl.metadata (2.8 kB)\n",
      "Requirement already satisfied: psutil>=5.9.8 in d:\\anaconda\\lib\\site-packages (from pandas-gbq) (7.0.0)\n",
      "Collecting google-auth-oauthlib>=0.7.0 (from pandas-gbq)\n",
      "  Downloading google_auth_oauthlib-1.4.0-py3-none-any.whl.metadata (2.6 kB)\n",
      "Requirement already satisfied: pytz>=2020.1 in d:\\anaconda\\lib\\site-packages (from pandas>=1.5.3->pandas-gbq) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in d:\\anaconda\\lib\\site-packages (from pandas>=1.5.3->pandas-gbq) (2025.2)\n",
      "Requirement already satisfied: cffi>=2.0.0 in d:\\anaconda\\lib\\site-packages (from cryptography>=38.0.3->google-auth<3.0.0,>=2.14.1->google-auth[pyopenssl]<3.0.0,>=2.14.1->google-cloud-bigquery) (2.0.0)\n",
      "Requirement already satisfied: pycparser in d:\\anaconda\\lib\\site-packages (from cffi>=2.0.0->cryptography>=38.0.3->google-auth<3.0.0,>=2.14.1->google-auth[pyopenssl]<3.0.0,>=2.14.1->google-cloud-bigquery) (2.23)\n",
      "Collecting requests-oauthlib>=0.7.0 (from google-auth-oauthlib>=0.7.0->pandas-gbq)\n",
      "  Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)\n",
      "Requirement already satisfied: pyasn1<0.7.0,>=0.6.1 in d:\\anaconda\\lib\\site-packages (from pyasn1-modules>=0.2.1->google-auth<3.0.0,>=2.14.1->google-auth[pyopenssl]<3.0.0,>=2.14.1->google-cloud-bigquery) (0.6.1)\n",
      "Collecting oauthlib>=3.0.0 (from requests-oauthlib>=0.7.0->google-auth-oauthlib>=0.7.0->pandas-gbq)\n",
      "  Downloading oauthlib-3.3.1-py3-none-any.whl.metadata (7.9 kB)\n",
      "Downloading google_cloud_bigquery-3.42.1-py3-none-any.whl (263 kB)\n",
      "Downloading google_api_core-2.31.0-py3-none-any.whl (173 kB)\n",
      "Downloading google_auth-2.55.1-py3-none-any.whl (252 kB)\n",
      "Downloading google_cloud_core-2.6.0-py3-none-any.whl (29 kB)\n",
      "Downloading google_resumable_media-2.10.0-py3-none-any.whl (81 kB)\n",
      "Downloading google_crc32c-1.8.0-cp313-cp313-win_amd64.whl (34 kB)\n",
      "Downloading googleapis_common_protos-1.75.0-py3-none-any.whl (300 kB)\n",
      "Downloading grpcio-1.81.1-cp313-cp313-win_amd64.whl (4.9 MB)\n",
      "   ---------------------------------------- 0.0/4.9 MB ? eta -:--:--\n",
      "   ---------------------------------------- 4.9/4.9 MB 40.8 MB/s  0:00:00\n",
      "Downloading grpcio_status-1.81.1-py3-none-any.whl (14 kB)\n",
      "Downloading proto_plus-1.28.0-py3-none-any.whl (50 kB)\n",
      "Downloading protobuf-7.35.1-cp310-abi3-win_amd64.whl (439 kB)\n",
      "Downloading requests-2.34.2-py3-none-any.whl (73 kB)\n",
      "Downloading pandas_gbq-0.35.0-py3-none-any.whl (50 kB)\n",
      "Downloading db_dtypes-1.7.0-py3-none-any.whl (17 kB)\n",
      "Downloading google_auth_oauthlib-1.4.0-py3-none-any.whl (19 kB)\n",
      "Downloading pydata_google_auth-1.9.1-py2.py3-none-any.whl (15 kB)\n",
      "Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)\n",
      "Downloading oauthlib-3.3.1-py3-none-any.whl (160 kB)\n",
      "Installing collected packages: requests, protobuf, oauthlib, grpcio, google-crc32c, requests-oauthlib, proto-plus, googleapis-common-protos, google-resumable-media, grpcio-status, google-auth, db-dtypes, google-auth-oauthlib, google-api-core, pydata-google-auth, google-cloud-core, google-cloud-bigquery, pandas-gbq\n",
      "\n",
      "  Attempting uninstall: requests\n",
      "\n",
      "    Found existing installation: requests 2.32.5\n",
      "\n",
      "    Uninstalling requests-2.32.5:\n",
      "\n",
      "      Successfully uninstalled requests-2.32.5\n",
      "\n",
      "   ----------------------------------------  0/18 [requests]\n",
      "  Attempting uninstall: protobuf\n",
      "   ----------------------------------------  0/18 [requests]\n",
      "    Found existing installation: protobuf 5.29.3\n",
      "   ----------------------------------------  0/18 [requests]\n",
      "   -- -------------------------------------  1/18 [protobuf]\n",
      "    Uninstalling protobuf-5.29.3:\n",
      "   -- -------------------------------------  1/18 [protobuf]\n",
      "      Successfully uninstalled protobuf-5.29.3\n",
      "   -- -------------------------------------  1/18 [protobuf]\n",
      "   -- -------------------------------------  1/18 [protobuf]\n",
      "   -- -------------------------------------  1/18 [protobuf]\n",
      "   -- -------------------------------------  1/18 [protobuf]\n",
      "   -- -------------------------------------  1/18 [protobuf]\n",
      "   -- -------------------------------------  1/18 [protobuf]\n",
      "   ---- -----------------------------------  2/18 [oauthlib]\n",
      "   ---- -----------------------------------  2/18 [oauthlib]\n",
      "   ---- -----------------------------------  2/18 [oauthlib]\n",
      "   ---- -----------------------------------  2/18 [oauthlib]\n",
      "   ---- -----------------------------------  2/18 [oauthlib]\n",
      "   ---- -----------------------------------  2/18 [oauthlib]\n",
      "   ------ ---------------------------------  3/18 [grpcio]\n",
      "   ------ ---------------------------------  3/18 [grpcio]\n",
      "   ------ ---------------------------------  3/18 [grpcio]\n",
      "   ------ ---------------------------------  3/18 [grpcio]\n",
      "   -------- -------------------------------  4/18 [google-crc32c]\n",
      "   ----------- ----------------------------  5/18 [requests-oauthlib]\n",
      "   ------------- --------------------------  6/18 [proto-plus]\n",
      "   ------------- --------------------------  6/18 [proto-plus]\n",
      "   --------------- ------------------------  7/18 [googleapis-common-protos]\n",
      "   --------------- ------------------------  7/18 [googleapis-common-protos]\n",
      "   --------------- ------------------------  7/18 [googleapis-common-protos]\n",
      "   --------------- ------------------------  7/18 [googleapis-common-protos]\n",
      "   --------------- ------------------------  7/18 [googleapis-common-protos]\n",
      "   --------------- ------------------------  7/18 [googleapis-common-protos]\n",
      "   --------------- ------------------------  7/18 [googleapis-common-protos]\n",
      "   --------------- ------------------------  7/18 [googleapis-common-protos]\n",
      "   ----------------- ----------------------  8/18 [google-resumable-media]\n",
      "   -------------------- -------------------  9/18 [grpcio-status]\n",
      "   ---------------------- ----------------- 10/18 [google-auth]\n",
      "   ---------------------- ----------------- 10/18 [google-auth]\n",
      "   ---------------------- ----------------- 10/18 [google-auth]\n",
      "   ---------------------- ----------------- 10/18 [google-auth]\n",
      "   ---------------------- ----------------- 10/18 [google-auth]\n",
      "   ---------------------- ----------------- 10/18 [google-auth]\n",
      "   ------------------------ --------------- 11/18 [db-dtypes]\n",
      "   ---------------------------- ----------- 13/18 [google-api-core]\n",
      "   ---------------------------- ----------- 13/18 [google-api-core]\n",
      "   ---------------------------- ----------- 13/18 [google-api-core]\n",
      "   ---------------------------- ----------- 13/18 [google-api-core]\n",
      "   ---------------------------- ----------- 13/18 [google-api-core]\n",
      "   ------------------------------- -------- 14/18 [pydata-google-auth]\n",
      "   ----------------------------------- ---- 16/18 [google-cloud-bigquery]\n",
      "   ----------------------------------- ---- 16/18 [google-cloud-bigquery]\n",
      "   ----------------------------------- ---- 16/18 [google-cloud-bigquery]\n",
      "   ----------------------------------- ---- 16/18 [google-cloud-bigquery]\n",
      "   ----------------------------------- ---- 16/18 [google-cloud-bigquery]\n",
      "   ------------------------------------- -- 17/18 [pandas-gbq]\n",
      "   ------------------------------------- -- 17/18 [pandas-gbq]\n",
      "   ---------------------------------------- 18/18 [pandas-gbq]\n",
      "\n",
      "Successfully installed db-dtypes-1.7.0 google-api-core-2.31.0 google-auth-2.55.1 google-auth-oauthlib-1.4.0 google-cloud-bigquery-3.42.1 google-cloud-core-2.6.0 google-crc32c-1.8.0 google-resumable-media-2.10.0 googleapis-common-protos-1.75.0 grpcio-1.81.1 grpcio-status-1.81.1 oauthlib-3.3.1 pandas-gbq-0.35.0 proto-plus-1.28.0 protobuf-7.35.1 pydata-google-auth-1.9.1 requests-2.34.2 requests-oauthlib-2.0.0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
      "streamlit 1.51.0 requires protobuf<7,>=3.20, but you have protobuf 7.35.1 which is incompatible.\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas\n",
    "!pip install google-cloud-bigquery pandas-gbq\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d412fb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tìm thấy 9 file. Đang tiến hành đẩy từng file lên mây...\n",
      "Đang đẩy file 'olist_customers_dataset.csv' lên bảng 'pineline_1.olist_customers_dataset'...\n",
      "Đang đẩy dữ liệu lên BigQuery tại bảng pineline_1.olist_customers_dataset...\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Viet Anh\\AppData\\Local\\Temp\\ipykernel_16404\\3617831008.py:38: FutureWarning: to_gbq is deprecated and will be removed in a future version. Please use pandas_gbq.to_gbq instead: https://pandas-gbq.readthedocs.io/en/latest/api.html#pandas_gbq.to_gbq\n",
      "  df.to_gbq(\n",
      "100%|██████████| 1/1 [00:00<00:00, 17623.13it/s]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  -> ✅ Đã đẩy xong bảng olist_customers_dataset gồm 99441 dòng.\n",
      "Đang đẩy file 'olist_geolocation_dataset.csv' lên bảng 'pineline_1.olist_geolocation_dataset'...\n",
      "Đang đẩy dữ liệu lên BigQuery tại bảng pineline_1.olist_geolocation_dataset...\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Viet Anh\\AppData\\Local\\Temp\\ipykernel_16404\\3617831008.py:38: FutureWarning: to_gbq is deprecated and will be removed in a future version. Please use pandas_gbq.to_gbq instead: https://pandas-gbq.readthedocs.io/en/latest/api.html#pandas_gbq.to_gbq\n",
      "  df.to_gbq(\n",
      "100%|██████████| 1/1 [00:00<00:00, 18978.75it/s]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  -> ✅ Đã đẩy xong bảng olist_geolocation_dataset gồm 1000163 dòng.\n",
      "Đang đẩy file 'olist_orders_dataset.csv' lên bảng 'pineline_1.olist_orders_dataset'...\n",
      "Đang đẩy dữ liệu lên BigQuery tại bảng pineline_1.olist_orders_dataset...\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Viet Anh\\AppData\\Local\\Temp\\ipykernel_16404\\3617831008.py:38: FutureWarning: to_gbq is deprecated and will be removed in a future version. Please use pandas_gbq.to_gbq instead: https://pandas-gbq.readthedocs.io/en/latest/api.html#pandas_gbq.to_gbq\n",
      "  df.to_gbq(\n",
      "100%|██████████| 1/1 [00:00<00:00, 19784.45it/s]\n",
      "C:\\Users\\Viet Anh\\AppData\\Local\\Temp\\ipykernel_16404\\3617831008.py:38: FutureWarning: to_gbq is deprecated and will be removed in a future version. Please use pandas_gbq.to_gbq instead: https://pandas-gbq.readthedocs.io/en/latest/api.html#pandas_gbq.to_gbq\n",
      "  df.to_gbq(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  -> ✅ Đã đẩy xong bảng olist_orders_dataset gồm 99441 dòng.\n",
      "Đang đẩy file 'olist_order_items_dataset.csv' lên bảng 'pineline_1.olist_order_items_dataset'...\n",
      "Đang đẩy dữ liệu lên BigQuery tại bảng pineline_1.olist_order_items_dataset...\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████| 1/1 [00:00<00:00, 7244.05it/s]\n",
      "C:\\Users\\Viet Anh\\AppData\\Local\\Temp\\ipykernel_16404\\3617831008.py:38: FutureWarning: to_gbq is deprecated and will be removed in a future version. Please use pandas_gbq.to_gbq instead: https://pandas-gbq.readthedocs.io/en/latest/api.html#pandas_gbq.to_gbq\n",
      "  df.to_gbq(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  -> ✅ Đã đẩy xong bảng olist_order_items_dataset gồm 112650 dòng.\n",
      "Đang đẩy file 'olist_order_payments_dataset.csv' lên bảng 'pineline_1.olist_order_payments_dataset'...\n",
      "Đang đẩy dữ liệu lên BigQuery tại bảng pineline_1.olist_order_payments_dataset...\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████| 1/1 [00:00<00:00, 6512.89it/s]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  -> ✅ Đã đẩy xong bảng olist_order_payments_dataset gồm 103886 dòng.\n",
      "Đang đẩy file 'olist_order_reviews_dataset.csv' lên bảng 'pineline_1.olist_order_reviews_dataset'...\n",
      "Đang đẩy dữ liệu lên BigQuery tại bảng pineline_1.olist_order_reviews_dataset...\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Viet Anh\\AppData\\Local\\Temp\\ipykernel_16404\\3617831008.py:38: FutureWarning: to_gbq is deprecated and will be removed in a future version. Please use pandas_gbq.to_gbq instead: https://pandas-gbq.readthedocs.io/en/latest/api.html#pandas_gbq.to_gbq\n",
      "  df.to_gbq(\n",
      "100%|██████████| 1/1 [00:00<00:00, 4609.13it/s]\n",
      "C:\\Users\\Viet Anh\\AppData\\Local\\Temp\\ipykernel_16404\\3617831008.py:38: FutureWarning: to_gbq is deprecated and will be removed in a future version. Please use pandas_gbq.to_gbq instead: https://pandas-gbq.readthedocs.io/en/latest/api.html#pandas_gbq.to_gbq\n",
      "  df.to_gbq(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  -> ✅ Đã đẩy xong bảng olist_order_reviews_dataset gồm 99224 dòng.\n",
      "Đang đẩy file 'olist_products_dataset.csv' lên bảng 'pineline_1.olist_products_dataset'...\n",
      "Đang đẩy dữ liệu lên BigQuery tại bảng pineline_1.olist_products_dataset...\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████| 1/1 [00:00<00:00, 6808.94it/s]\n",
      "C:\\Users\\Viet Anh\\AppData\\Local\\Temp\\ipykernel_16404\\3617831008.py:38: FutureWarning: to_gbq is deprecated and will be removed in a future version. Please use pandas_gbq.to_gbq instead: https://pandas-gbq.readthedocs.io/en/latest/api.html#pandas_gbq.to_gbq\n",
      "  df.to_gbq(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  -> ✅ Đã đẩy xong bảng olist_products_dataset gồm 32951 dòng.\n",
      "Đang đẩy file 'olist_sellers_dataset.csv' lên bảng 'pineline_1.olist_sellers_dataset'...\n",
      "Đang đẩy dữ liệu lên BigQuery tại bảng pineline_1.olist_sellers_dataset...\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████| 1/1 [00:00<00:00, 5475.59it/s]\n",
      "C:\\Users\\Viet Anh\\AppData\\Local\\Temp\\ipykernel_16404\\3617831008.py:38: FutureWarning: to_gbq is deprecated and will be removed in a future version. Please use pandas_gbq.to_gbq instead: https://pandas-gbq.readthedocs.io/en/latest/api.html#pandas_gbq.to_gbq\n",
      "  df.to_gbq(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  -> ✅ Đã đẩy xong bảng olist_sellers_dataset gồm 3095 dòng.\n",
      "Đang đẩy file 'product_category_name_translation.csv' lên bảng 'pineline_1.product_category_name_translation'...\n",
      "Đang đẩy dữ liệu lên BigQuery tại bảng pineline_1.product_category_name_translation...\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████| 1/1 [00:00<00:00, 15592.21it/s]"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  -> ✅ Đã đẩy xong bảng product_category_name_translation gồm 71 dòng.\n",
      "🎉 Tèn ten! Đã đẩy toàn bộ folder lên BigQuery thành công!\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "import glob\n",
    "\n",
    "def day_du_lieu_len_bigquery():\n",
    "    # 1. API KEY\n",
    "    # Thay đường dẫn này bằng file JSON.\n",
    "    os.environ[\"GOOGLE_APPLICATION_CREDENTIALS\"] = r\"E:\\4. Khoá Học Phân Tích Dữ Liệu\\3. Bài làm BigProject để đưa vào CV\\Big Project 01\\Project 01 - Ecomerce\\key.json\"\n",
    "    \n",
    "    # 2. ĐỌC DỮ LIỆU TỪ MÁY TÍNH \n",
    "    # Dùng glob để quét toàn bộ file csv trong folder\n",
    "    folder_path = r\"E:\\4. Khoá Học Phân Tích Dữ Liệu\\3. Bài làm BigProject để đưa vào CV\\Big Project 01\\Project 01 - Ecomerce\\Dataset\"\n",
    "    all_files = glob.glob(os.path.join(glob.escape(folder_path), \"*.csv\"))\n",
    "    print(f\"Tìm thấy {len(all_files)} file. Đang tiến hành đẩy từng file lên mây...\")\n",
    "        \n",
    "    # 3. KHAI BÁO ĐỊA CHỈ TRÊN BIGQUERY\n",
    "    # Thay 'project_id' bằng ID dự án trên Google Cloud\n",
    "    project_id = \"bva-data-pineline-1\" \n",
    "    \n",
    "    # Cấu trúc: dataset_name.table_name\n",
    "    dataset_name = \"pineline_1\"\n",
    "    # 4. TẠO VÒNG LẶP CHỞ TỪNG FILE\n",
    "    for file in all_files:\n",
    "        # Lấy tên file gốc để làm tên bảng (Ví dụ: 'facebook_ads.csv' -> 'facebook_ads')\n",
    "        ten_file_goc = os.path.basename(file)\n",
    "        ten_bang = ten_file_goc.replace('.csv', '')\n",
    "        # Đọc dữ liệu của 1 file duy nhất\n",
    "        df = pd.read_csv(file)\n",
    "        # Cấu trúc địa chỉ: dataset_name.table_name\n",
    "        Table_name = f\"{dataset_name}.{ten_bang}\"\n",
    "        print(f\"Đang đẩy file '{ten_file_goc}' lên bảng '{Table_name}'...\")\n",
    "    # 5. ĐẨY DỮ LIỆU LÊN DATAWAREHOUSE\n",
    "        print(f\"Đang đẩy dữ liệu lên BigQuery tại bảng {Table_name}...\")\n",
    "    # Hàm to_gbq() là hàm đưa dữ liệu lên Google BigQuery\n",
    "    # if_exists='replace': Nếu bảng đã có sẵn thì xóa đi ghi đè lên. \n",
    "    # (Có thể đổi thành 'append' nếu muốn nối thêm dữ liệu mới vào bảng cũ)\n",
    "        df.to_gbq(\n",
    "            destination_table=Table_name,\n",
    "            project_id=project_id,\n",
    "            if_exists='replace'\n",
    "        )\n",
    "        print(f\"  -> ✅ Đã đẩy xong bảng {ten_bang} gồm {len(df)} dòng.\")\n",
    "    print(\"🎉 Tèn ten! Đã đẩy toàn bộ folder lên BigQuery thành công!\")\n",
    "\n",
    "# Chạy thử \n",
    "day_du_lieu_len_bigquery()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "75ad813d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44685726",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01ed219e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f5dc345",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9aa51753",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "359bd763",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8339d21d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
