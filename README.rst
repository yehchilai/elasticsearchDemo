elasticsearchDemo
=================

Python setup
------------

Install requirement

.. code-block:: bash

  $ pip install -r requirements.txt


(Optional) use virtual environment

.. code-block:: bash

  $ virtualenv venv
  $ source venv/bin/ctivate
  $ pip install -r requirements.txt

Elasticsearch and Kibana environment setup
------------------------------------------

Use docker to run the elasticsearch and Kibana.

.. code-block:: bash

  $ docker-compose up

Insert demo data into elasticsearch 

.. code-block:: bash

  $ cd data
  $ curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/bank/account/_bulk?pretty' --data-binary @accounts.json


Run the demo
------------

Run a simple search with aggregation.

.. code-block:: bash

  $ python client/client.py

If use virtual environment.

.. code-block:: bash
  
  $ source venv/bin/activate
  (venv)$ python client/client.py