organizations-edx-platform-extensions
=====================================

Notice: This repo will be archived in April 2021.
#######

organizations-edx-platform-extensions (``edx_solutions_organizations``) is a Django application responsible for managing the concept of Organizations in the Open edX platform. Organizations represent the entities responsible for creating and publishing Courses. In the future the scope and responsibilty of the Organization may evolve to include other aspects, such as related learners.


Open edX Platform Integration
-----------------------------
1. Update the version of ``organizations-edx-platform-extensions`` in the appropriate requirements file (e.g. ``requirements/edx/custom.txt``).
2. Add ‘edx_solutions_organizations’ to the list of installed apps in ``common.py``.
3. Install organizations app via requirements file

.. code-block:: bash
  $ pip install -r requirements/edx/custom.txt

4. (Optional) Run tests:

.. code-block:: bash

   $ paver test_system -s lms -t edx_solutions_organizations

