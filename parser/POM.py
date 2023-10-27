import xml.etree.ElementTree as ET


def find_all_children(element, tag):
    children = []
    element_tag = f"{element.tag.split('}')[1]}" if "}" in element.tag else element.tag
    if element_tag == tag:
        children.append(element)

    for child in element:
        children.extend(find_all_children(child, tag))

    return children


class POM:
    def __init__(self, file) -> None:
        self.file = file
        self.namespace = {"mvn": "http://maven.apache.org/POM/4.0.0"}
        self.root = ET.fromstring(self.file.decoded_content.decode())
        self.properties = {}
        self.dependencies = {}
        self.path = file.path
        self.download_url = file.download_url

    def parse_properties(self) -> None:
        for child in self.root.findall("mvn:properties/*", self.namespace):
            tag_name = f'{child.tag.split("}")[1]}' if "}" in child.tag else child.tag
            value = child.text
            self.properties[tag_name] = value

        for key, value in self.properties.items():
            self.resolve_version(key, value)

    def resolve_version(self, property, version):
        if version.startswith("${"):
            v = self.resolve_version(version[2:-1], self.properties[version[2:-1]])
            self.properties[property] = v

            return v
        else:
            return version

    def get_properties(self):
        self.parse_properties()

        return self.properties

    def parse_depenencies(self):
        self.fetch_namespace()

        dependencies_content = find_all_children(self.root, "dependency")

        self.parse_properties()

        for dependency in dependencies_content:
            # print(dependency.find("mvn:groupId", self.namespace).text)
            groupId = dependency.find("mvn:groupId", self.namespace).text
            artifactId = dependency.find("mvn:artifactId", self.namespace).text
            version_elem = dependency.find("mvn:version", self.namespace)
            version = (
                version_elem.text
                if version_elem is not None
                else "Version not specified"
            )

            version = (
                self.properties[version[2:-1]] if version.startswith("${") else version
            )

            if groupId in self.dependencies:
                self.dependencies[groupId].append(
                    {"artifactId": artifactId, "version": version}
                )
            else:
                self.dependencies[groupId] = [
                    {"artifactId": artifactId, "version": version}
                ]

    def fetch_namespace(self):
        self.namespace = {"mvn": self.root.tag.split("}")[0][1:]}
