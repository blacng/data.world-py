from pprint import pformat
from six import iteritems


class ProjectSummaryResponse(object):

    swagger_types = {
        'title': 'str',
        'objective': 'str',
        'summary': 'str',
        'license': 'str',
        'tags': 'list[str]',
        'files': 'list[FileSummaryResponse]',
        'linked_datasets': 'list[LinkedDatasetSummaryResponse]',
        'visibility': 'str',
        'status': 'str',
        'owner': 'str',
        'id': 'str',
        'created': 'str',
        'updated': 'str',
        'access_level': 'str'
    }

    attribute_map = {
        'title': 'title',
        'objective': 'objective',
        'summary': 'summary',
        'license': 'license',
        'tags': 'tags',
        'files': 'files',
        'linked_datasets': 'linkedDatasets',
        'visibility': 'visibility',
        'status': 'status',
        'owner': 'owner',
        'id': 'id',
        'created': 'created',
        'updated': 'updated',
        'access_level': 'accessLevel'
    }

    def __init__(self, title=None, objective=None, summary=None,
                 license=None, tags=None, files=None, linked_datasets=None,
                 visibility=None, status=None, owner=None, id=None,
                 created=None, updated=None, access_level=None):
        self._title = None
        self._objective = None
        self._summary = None
        self._license = None
        self._tags = None
        self._files = None
        self._linked_datasets = None
        self._visibility = None
        self._status = None
        self._owner = None
        self._id = None
        self._created = None
        self._updated = None
        self._access_level = None

        self.title = title
        if objective is not None:
            self.objective = objective
        if summary is not None:
            self.summary = summary
        if license is not None:
            self.license = license
        if tags is not None:
            self.tags = tags
        if files is not None:
            self.files = files
        if linked_datasets is not None:
            self.linked_datasets = linked_datasets
        self.visibility = visibility
        self.status = status
        self.owner = owner
        self.id = id
        self.created = created
        self.updated = updated
        self.access_level = access_level

    @property
    def title(self):
        """
        Gets the title of this ProjectSummaryResponse.
        :return: The title of this ProjectSummaryResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ProjectSummaryResponse.
        :param title: The title of this ProjectSummaryResponse.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def objective(self):
        """
        Gets the objective of this ProjectSummaryResponse.
        :return: The objective of this ProjectSummaryResponse.
        :rtype: str
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """
        Sets the objective of this ProjectSummaryResponse.
        :param objective: The objective of this ProjectSummaryResponse.
        :type: str
        """

        self._objective = objective

    @property
    def summary(self):
        """
        Gets the summary of this ProjectSummaryResponse.
        :return: The summary of this ProjectSummaryResponse.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this ProjectSummaryResponse.
        :param summary: The summary of this ProjectSummaryResponse.
        :type: str
        """

        self._summary = summary

    @property
    def license(self):
        """
        Gets the license of this ProjectSummaryResponse.
        :return: The license of this ProjectSummaryResponse.
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """
        Sets the license of this ProjectSummaryResponse.
        :param license: The license of this ProjectSummaryResponse.
        :type: str
        """

        self._license = license

    @property
    def tags(self):
        """
        Gets the tags of this ProjectSummaryResponse.
        :return: The tags of this ProjectSummaryResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ProjectSummaryResponse.
        :param tags: The tags of this ProjectSummaryResponse.
        :type: list[str]
        """

        self._tags = tags

    @property
    def files(self):
        """
        Gets the files of this ProjectSummaryResponse.
        :return: The files of this ProjectSummaryResponse.
        :rtype: list[FileSummaryResponse]
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this ProjectSummaryResponse.
        :param files: The files of this ProjectSummaryResponse.
        :type: list[FileSummaryResponse]
        """

        self._files = files

    @property
    def linked_datasets(self):
        """
        Gets the linked_datasets of this ProjectSummaryResponse.
        :return: The linked_datasets of this ProjectSummaryResponse.
        :rtype: list[LinkedDatasetSummaryResponse]
        """
        return self._linked_datasets

    @linked_datasets.setter
    def linked_datasets(self, linked_datasets):
        """
        Sets the linked_datasets of ProjectSummaryResponse
        :param linked_datasets: The linked_datasets of ProjectSummaryResponse
        :type: list[LinkedDatasetSummaryResponse]
        """

        self._linked_datasets = linked_datasets

    @property
    def visibility(self):
        """
        Gets the visibility of this ProjectSummaryResponse.
        :return: The visibility of this ProjectSummaryResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """
        Sets the visibility of this ProjectSummaryResponse.
        :param visibility: The visibility of this ProjectSummaryResponse.
        :type: str
        """
        if visibility is None:
            raise ValueError("Invalid value for `visibility`, " +
                             "must not be `None`")
        self._visibility = visibility

    @property
    def status(self):
        """
        Gets the status of this ProjectSummaryResponse.
        Processing status of project. This status can be checked periodically
        after changes are made to the project to determine the status of
        asynchronous processing.  * `NEW`: Just created. Not yet processed.
        * `INPROGRESS`: Currently being processed.
        * `LOADED`: Successfully processed.
        * `SYSTEMERROR`: Error state due to processing failure.
        :return: The status of this ProjectSummaryResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ProjectSummaryResponse.
        Processing status of project.
        This status can be checked periodically after changes are made to the
        project to determine the status of asynchronous processing.
        * `NEW`: Just created. Not yet processed.
        * `INPROGRESS`: Currently being processed.
        * `LOADED`: Successfully processed.
        * `SYSTEMERROR`: Error state due to processing failure.
        :param status: The status of this ProjectSummaryResponse.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, " +
                             "must not be `None`")
        self._status = status

    @property
    def owner(self):
        """
        Gets the owner of this ProjectSummaryResponse.
        :return: The owner of this ProjectSummaryResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this ProjectSummaryResponse.
        :param owner: The owner of this ProjectSummaryResponse.
        :type: str
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")

        self._owner = owner

    @property
    def id(self):
        """
        Gets the id of this ProjectSummaryResponse.
        :return: The id of this ProjectSummaryResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProjectSummaryResponse.
        :param id: The id of this ProjectSummaryResponse.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def created(self):
        """
        Gets the created of this ProjectSummaryResponse.
        :return: The created of this ProjectSummaryResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this ProjectSummaryResponse.
        :param created: The created of this ProjectSummaryResponse.
        :type: str
        """
        if created is None:
            raise ValueError("Invalid value for `created`, " +
                             "must not be `None`")
        self._created = created

    @property
    def updated(self):
        """
        Gets the updated of this ProjectSummaryResponse.
        :return: The updated of this ProjectSummaryResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this ProjectSummaryResponse.
        :param updated: The updated of this ProjectSummaryResponse.
        :type: str
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, " +
                             "must not be `None`")
        self._updated = updated

    @property
    def access_level(self):
        """
        Gets the access_level of this ProjectSummaryResponse.
        :return: The access_level of this ProjectSummaryResponse.
        :rtype: str
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """
        Sets the access_level of this ProjectSummaryResponse.
        :param access_level: The access_level of this ProjectSummaryResponse.
        :type: str
        """
        if access_level is None:
            raise ValueError("Invalid value for `access_level`," +
                             "must not be `None`")
        self._access_level = access_level

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ProjectSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other