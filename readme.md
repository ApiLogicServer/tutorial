&nbsp;&nbsp;&nbsp;

# Learning or Teaching Python??

<details markdown>

&nbsp;

<summary>Learn By Example</summary>

Tutorials are useful ways to learn, but the __key concepts__ can be overshadowed by mechanics, and often don't include the real-world __IDE experience__.

Here we take a different approach: a __running app__ you can explore, using the table below:

* Explore code samples for key technology areas
* In a _running_ project
* That you can experiment with (debug, alter...)

To __explore code__, click the _Sample Code_ link - that will open that code file.

To __run__, use the Run/Debug configurations ("play" button, upper left).  There are 2 web apps you can run:

* API Logic Server - __automated__ by API Logic server (see next section)

* Raw Flask - a __hand-coded__ web app with minimal functionality

</details>

&nbsp;

<details markdown>


<summary>Manual Coding vs. Automation?  Yes.</summary>

&nbsp;

Frameworks (like Flask) are flexible, but time-consuming and complex.

Low-code solutions save time, but can be inflexible and not compatible with tools like your IDE.

API Logic Server has a different approach that delivers the best of both worlds:

1. __Automation__, to create a complete web-app based on your schema:

    * an API - endpoint for every table, CRUD functions including filtering, pagination and related data
    * an Admin Web App - multi-page, multi-table apps with page transitions, lookups and declarative hide/show
2. Builds a __customizable project__ you can extend and debug with _your_ IDE
3. __Unique spreadsheet-like business rules__ for backend logic - 40X more concise than code

The app here would have take several weeks to build.  API Logic Server created it with 1 command, and then added a few API and logic customizations for you to explore.

* Try the [Tutorial](Tutorial.md)
</details>


&nbsp;

<p align="center">
  <h2 align="center">Topics</h2>
</p>

&nbsp;


| Tech Area | Skill | Sample Code    | Notes   |
|:---- |:------|:-----------|:--------|
| __Flask__ | Setup | [```flask_basic.py```](Basic_app/flask_basic.py) | also shows end points, events  |
|  | Events | [```api/customize_api.py```](ApiLogicProject/api_logic_server_run.py) |  see `flask_events` |
| __API__ | Create End Point | [```flask_basic.py```](Basic_app/flask_basic.py)<br>[```api/customize_api.py```](ApiLogicProject/api/customize_api.py) |  see `def order():` |
|  | Call endpoint | [```test/.../place_order.py```](ApiLogicProject/test/api_logic_server_behave/features/steps/place_order.py) |   |
| __Config__ | Config | [```config.py```](ApiLogicProject/config.py) |   |
|  | Env variables | [```config.py```](ApiLogicProject/config.py) | os.getenv(...)  |
| __SQLAlchemy__ | Data Model Classes | [```database/customize_models.py```](ApiLogicProject/database/customize_models.py) |   |
|  | Read / Write | [```api/customize_api.py```](ApiLogicProject/api/customize_api.py) | see `def order():`  |
|  | Multiple Databases | [```database/bind_databases.py```](ApiLogicProject/database/bind_databases.py) |    |
|  | Events | [```security/system/security_manager.py```](ApiLogicProject/security/system/security_manager.py) |    |
| __Behave__ | Testing | [```test/.../place_order.py```](ApiLogicProject/test/api_logic_server_behave/features/steps/place_order.py) |   |
| __Alembic__ | Schema Changes | [```database/alembic/readme.md```](ApiLogicProject/database/alembic/readme.md) |   |
| __Docker__ | Dev Env | [```.devcontainer/devcontainer.json```](.devcontainer/devcontainer.json) | See also "dockerFile":... |
|  | Containerize Project | [```devops/docker/build-container.dockerfile```](ApiLogicProject/devops/docker/build-container.dockerfile) |  |