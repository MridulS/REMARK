# Script to find the all the requirements of REMARKs
import os

# Places the requirements file can be placed inside a REMARK
ALLOWED_PATHS = ["/Binder/requirements.txt", "/requirements.txt"]


def find_union_requirements():
    """ Find the union of all the requirements to create a Binder
    environement which can run all the REMARKs, if launched through
    https://github.com/econ-ark/remark.

    Returns
    -------
    requirements: Union of set of requirements
    """
    requirements = set()
    # Find all the REMARKs
    for remark in next(os.walk("REMARKs/"))[1]:
        binder_path = "REMARKs/" + remark + ALLOWED_PATHS[0]
        require_path = "REMARKs/" + remark + ALLOWED_PATHS[1]
        if os.path.isfile(binder_path):
            with open(binder_path, "r") as f:
                for line in f:
                    requirements.add(line)
        elif os.path.isfile(require_path):
            with open(require_path, "r") as f:
                for line in f:
                    requirements.add(line)
        else:
            # TODO
            # This should error out once every REMARK follows the specification
            print(f"No requirements found for {remark}")
    return requirements


# create meta requirements file for REMARKs
requirements = find_union_requirements()
with open("requirements.txt", "w") as f:
    f.writelines("".join(requirements))
