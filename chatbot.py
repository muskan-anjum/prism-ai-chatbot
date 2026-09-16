services = {
    "website development": (
        "PRISM provides website development services for creating modern, "
        "responsive and user-friendly websites tailored to business requirements."
    ),

    "mobile app development": (
        "PRISM provides mobile app development services for building "
        "user-friendly mobile applications based on business requirements."
    ),

    "crm": (
        "PRISM provides CRM and ERP solutions that help businesses manage "
        "customers, operations, data and internal processes efficiently."
    ),

    "erp": (
        "PRISM provides CRM and ERP solutions that help businesses manage "
        "customers, operations, data and internal processes efficiently."
    ),

    "odoo": (
        "PRISM provides Odoo solutions to help businesses manage functions "
        "such as CRM, sales, inventory, accounting and other operations."
    ),

    "ai automation": (
        "PRISM provides AI automation solutions to automate repetitive "
        "business processes and improve operational efficiency."
    ),

    "ai chatbot": (
        "PRISM develops AI chatbot solutions that can interact with customers, "
        "answer queries and support business workflows."
    ),

    "digital marketing": (
        "PRISM provides digital marketing services to help businesses improve "
        "their online presence and reach customers through digital channels."
    ),

    "devops": (
        "PRISM provides DevOps and cloud solutions to support application "
        "deployment, infrastructure management and development workflows."
    ),

    "cloud": (
        "PRISM provides DevOps and cloud solutions to support application "
        "deployment, infrastructure management and development workflows."
    ),

    "blockchain": (
        "PRISM provides blockchain development solutions for businesses "
        "requiring secure and decentralized applications."
    )
}


def get_service_response(message):
    message = message.lower().strip()

    for keyword, response in services.items():
        if keyword in message:
            return response

    return (
        "I can help you with PRISM's services including Website Development, "
        "Mobile App Development, CRM/ERP, Odoo, AI Automation, AI Chatbots, "
        "Digital Marketing, DevOps/Cloud and Blockchain. "
        "Which service would you like to know more about?"
    )