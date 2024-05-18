def find_element_by_tag_name(driver, name, ignore_message=False):
    """
    Finds an element by tag name.

    :param driver: WebDriver instance
    :param name: Tag name to search for
    :param ignore_message: Whether to ignore the error message if the element is not found
    :return: WebElement if found, None otherwise
    """
    try:
        return driver.find_element_by_tag_name(name)
    except NoSuchElementException:
        if not ignore_message:
            raise NoSuchElementException(f"Element with tag name '{name}' not found")
        return None

