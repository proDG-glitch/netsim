"""Text and quiz assets for NetSim."""

from __future__ import annotations

from dataclasses import dataclass


FONT = {
    "A": [" ### ", "#   #", "#####", "#   #", "#   #"],
    "B": ["#### ", "#   #", "#### ", "#   #", "#### "],
    "C": [" ####", "#    ", "#    ", "#    ", " ####"],
    "D": ["#### ", "#   #", "#   #", "#   #", "#### "],
    "E": ["#####", "#    ", "#####", "#    ", "#####"],
    "F": ["#####", "#    ", "#####", "#    ", "#    "],
    "G": [" ####", "#    ", "# ###", "#   #", " ####"],
    "H": ["#   #", "#   #", "#####", "#   #", "#   #"],
    "I": ["#####", "  #  ", "  #  ", "  #  ", "#####"],
    "K": ["#   #", "#  # ", "###  ", "#  # ", "#   #"],
    "L": ["#    ", "#    ", "#    ", "#    ", "#####"],
    "M": ["#   #", "## ##", "# # #", "#   #", "#   #"],
    "N": ["#   #", "##  #", "# # #", "#  ##", "#   #"],
    "O": [" ### ", "#   #", "#   #", "#   #", " ### "],
    "P": ["#### ", "#   #", "#### ", "#    ", "#    "],
    "Q": [" ### ", "#   #", "#   #", "#  ##", " ####"],
    "R": ["#### ", "#   #", "#### ", "#  # ", "#   #"],
    "S": [" ####", "#    ", " ### ", "    #", "#### "],
    "T": ["#####", "  #  ", "  #  ", "  #  ", "  #  "],
    "U": ["#   #", "#   #", "#   #", "#   #", " ### "],
    "V": ["#   #", "#   #", "#   #", " # # ", "  #  "],
    "W": ["#   #", "#   #", "# # #", "## ##", "#   #"],
    "X": ["#   #", " # # ", "  #  ", " # # ", "#   #"],
    "Y": ["#   #", " # # ", "  #  ", "  #  ", "  #  "],
    "Z": ["#####", "   # ", "  #  ", " #   ", "#####"],
    "0": [" ### ", "#  ##", "# # #", "##  #", " ### "],
    "1": ["  #  ", " ##  ", "  #  ", "  #  ", "#####"],
    "2": [" ### ", "#   #", "   # ", "  #  ", "#####"],
    "3": ["#### ", "    #", " ### ", "    #", "#### "],
    "4": ["#   #", "#   #", "#####", "    #", "    #"],
    "7": ["#####", "   # ", "  #  ", " #   ", "#    "],
    "8": [" ### ", "#   #", " ### ", "#   #", " ### "],
    "9": [" ### ", "#   #", " ####", "    #", " ### "],
    "%": ["#   #", "   # ", "  #  ", " #   ", "#   #"],
    "?": [" ### ", "#   #", "   # ", "     ", "  #  "],
    " ": ["   ", "   ", "   ", "   ", "   "],
}


NETSIM_ASCII_HEADER = r"""
 ██████   █████ ██████████ ███████████  █████████  █████ ██████   ██████
▒▒██████ ▒▒███ ▒▒███▒▒▒▒▒█▒█▒▒▒███▒▒▒█ ███▒▒▒▒▒███▒▒███ ▒▒██████ ██████
 ▒███▒███ ▒███  ▒███  █ ▒ ▒   ▒███  ▒ ▒███    ▒▒▒  ▒███  ▒███▒█████▒███
 ▒███▒▒███▒███  ▒██████       ▒███    ▒▒█████████  ▒███  ▒███▒▒███ ▒███
 ▒███ ▒▒██████  ▒███▒▒█       ▒███     ▒▒▒▒▒▒▒▒███ ▒███  ▒███ ▒▒▒  ▒███
 ▒███  ▒▒█████  ▒███ ▒   █    ▒███     ███    ▒███ ▒███  ▒███      ▒███
 █████  ▒▒█████ ██████████    █████   ▒▒█████████  █████ █████     █████
▒▒▒▒▒    ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒     ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒ ▒▒▒▒▒     ▒▒▒▒▒
""".strip("\n")


LESSONS_ASCII_HEADER = r"""
 █████       ██████████  █████████   █████████     ███████    ██████   █████  █████████
▒▒███       ▒▒███▒▒▒▒▒█ ███▒▒▒▒▒███ ███▒▒▒▒▒███  ███▒▒▒▒▒███ ▒▒██████ ▒▒███  ███▒▒▒▒▒███
 ▒███        ▒███  █ ▒ ▒███    ▒▒▒ ▒███    ▒▒▒  ███     ▒▒███ ▒███▒███ ▒███ ▒███    ▒▒▒
 ▒███        ▒██████   ▒▒█████████ ▒▒█████████ ▒███      ▒███ ▒███▒▒███▒███ ▒▒█████████
 ▒███        ▒███▒▒█    ▒▒▒▒▒▒▒▒███ ▒▒▒▒▒▒▒▒███▒███      ▒███ ▒███ ▒▒██████  ▒▒▒▒▒▒▒▒███
 ▒███      █ ▒███ ▒   █ ███    ▒███ ███    ▒███▒▒███     ███  ▒███  ▒▒█████  ███    ▒███
 ███████████ ██████████▒▒█████████ ▒▒█████████  ▒▒▒███████▒   █████  ▒▒█████▒▒█████████
▒▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒
""".strip("\n")


HOME_INTRO = (
    "NetSim is a retro-styled learning console for cluster networking. "
    "Use the keyboard to move through sections, inspect diagrams, and work through "
    "short guided quizzes without ever leaving the terminal."
)

SIMULATION_TEXT = (
    "SIMULATION\n\n"
    "1. A user applies a network policy or workload manifest.\n"
    "2. The control plane stores desired state and notifies watchers.\n"
    "3. Scheduling and reconciliation place workloads and enforce intent.\n"
    "4. Node agents configure runtime, networking, and service reachability.\n"
    "5. Traffic begins to flow and operators verify the result.\n\n"
    "This screen is intentionally a placeholder for future guided exercises."
)

SCENARIOS_TEXT = (
    "SCENARIOS\n\n"
    "Packet loss drill\n"
    "- Pod-to-service latency spikes.\n"
    "- kube-proxy rules drift from expected state.\n"
    "- Operator compares desired routing with current endpoints.\n\n"
    "Node pressure drill\n"
    "- Worker Node 2 reports memory pressure.\n"
    "- New workloads are redirected to a healthier node.\n\n"
    "This area is ready for more scripted scenario flows."
)

HELP_TEXT = (
    "KEYS\n\n"
    "Up / Down: Move selection\n"
    "Enter: Open or confirm\n"
    "h: Home\n"
    "b: Back\n"
    "q: Quit\n"
    "1-4: Choose quiz answers on the detail screen\n"
    "0: Back or exit on supported screens\n\n"
    "The app is designed for keyboard-only use."
)


ARCHITECTURE_ITEMS = [
    {
        "key": "api_server",
        "label": "API SERVER",
        "role": "Central entry point that validates and stores desired state.",
        "details": (
            "The API server is the front door of the cluster. Every create, update, "
            "observe, and delete action flows through it before controllers or workers react."
        ),
    },
    {
        "key": "scheduler",
        "label": "SCHEDULER",
        "role": "Matches unscheduled Pods to nodes with available resources.",
        "details": (
            "The scheduler reads pending workloads and picks the node that best fits "
            "resource requests, policy rules, and placement constraints."
        ),
    },
    {
        "key": "controller_manager",
        "label": "CONTROLLER MANAGER",
        "role": "Continuously reconciles actual state toward desired state.",
        "details": (
            "Controllers compare what the cluster should look like with what actually exists, "
            "then issue corrective actions until they match."
        ),
    },
    {
        "key": "etcd",
        "label": "ETCD",
        "role": "Durable key-value store for cluster configuration and state.",
        "details": (
            "etcd holds the source of truth that the control plane relies on for cluster "
            "configuration, object definitions, and coordination metadata."
        ),
    },
    {
        "key": "worker_node_1",
        "label": "WORKER NODE 1",
        "role": "Executes workload Pods and reports health back to the control plane.",
        "details": (
            "Worker nodes host containers, connect services, and expose runtime state "
            "through kubelet and local network agents."
        ),
    },
    {
        "key": "worker_node_2",
        "label": "WORKER NODE 2",
        "role": "Provides redundant compute capacity and routing endpoints.",
        "details": (
            "A second worker helps NetSim show how workloads spread, fail over, and "
            "continue serving traffic under changing conditions."
        ),
    },
    {
        "key": "pod",
        "label": "PODS",
        "role": "Smallest deployable unit that carries one or more containers.",
        "details": (
            "Pods inherit scheduling decisions, IP connectivity, policies, and service "
            "discovery. They are where application traffic ultimately terminates."
        ),
    },
    {
        "key": "kubelet",
        "label": "KUBELET",
        "role": "Node agent that ensures declared Pods are actually running.",
        "details": (
            "kubelet watches assigned work, talks to the runtime, and reports status back "
            "to the API server so the control plane can keep reconciling."
        ),
    },
    {
        "key": "kube_proxy",
        "label": "KUBE-PROXY",
        "role": "Programs local service routing rules and connection paths.",
        "details": (
            "kube-proxy updates packet forwarding and service translation rules so cluster "
            "traffic can reach the right Pods behind virtual service addresses."
        ),
    },
]


TOPIC_DESCRIPTIONS = {
    "basics": "Foundations, vocabulary, and the mental model behind a clustered network platform.",
    "control_plane": "How API server, scheduler, and controllers cooperate to move the cluster forward.",
    "pods": "How Pods are scheduled, started, connected, and observed on worker nodes.",
    "networking": "How services, proxies, and routing rules move packets to the right destination.",
}


@dataclass(frozen=True)
class QuizQuestion:
    prompt: str
    options: tuple[str, str, str, str]
    correct_index: int
    explanation: str


@dataclass(frozen=True)
class QuizTopic:
    key: str
    title: str
    description: str
    art_label: str
    questions: tuple[QuizQuestion, ...]


QUIZ_TOPICS = (
    QuizTopic(
        key="basics",
        title="KUBERNETES BASICS",
        description=TOPIC_DESCRIPTIONS["basics"],
        art_label="NET",
        questions=(
            QuizQuestion(
                prompt="What best describes desired state in a cluster?",
                options=(
                    "THE LOGS EMITTED BY RUNNING PODS",
                    "THE CONFIGURATION THE CONTROL PLANE TRIES TO MAKE TRUE",
                    "THE IP ADDRESS CHOSEN FOR A SERVICE",
                    "THE CPU CURRENTLY CONSUMED BY A NODE",
                ),
                correct_index=1,
                explanation="Desired state is the declared target. Controllers work continuously to make the live cluster match it.",
            ),
            QuizQuestion(
                prompt="Why do operators use Pods instead of managing containers one by one?",
                options=(
                    "PODS ARE THE SCHEDULING AND NETWORKING UNIT KUBERNETES UNDERSTANDS",
                    "PODS ALWAYS CONTAIN EXACTLY FOUR CONTAINERS",
                    "PODS REPLACE THE NEED FOR A SCHEDULER",
                    "PODS DISABLE SERVICE DISCOVERY OVERHEAD",
                ),
                correct_index=0,
                explanation="Pods are the basic unit the platform schedules, connects to services, and observes as a workload target.",
            ),
        ),
    ),
    QuizTopic(
        key="control_plane",
        title="CONTROL PLANE",
        description=TOPIC_DESCRIPTIONS["control_plane"],
        art_label="CTRL",
        questions=(
            QuizQuestion(
                prompt="Which component chooses a node for an unscheduled Pod?",
                options=(
                    "KUBE-PROXY",
                    "ETCD",
                    "SCHEDULER",
                    "COREDNS",
                ),
                correct_index=2,
                explanation="The scheduler evaluates placement constraints and selects a worker node for pending Pods.",
            ),
            QuizQuestion(
                prompt="What is the controller manager primarily responsible for?",
                options=(
                    "RECONCILING ACTUAL STATE TOWARD DESIRED STATE",
                    "ENCRYPTING ALL CLUSTER TRAFFIC",
                    "BUILDING CONTAINER IMAGES",
                    "TERMINATING EVERY INCOMING USER SESSION",
                ),
                correct_index=0,
                explanation="Controllers watch resources and make repeated corrective actions until the cluster matches the intended specification.",
            ),
        ),
    ),
    QuizTopic(
        key="pods",
        title="PODS & WORKLOADS",
        description=TOPIC_DESCRIPTIONS["pods"],
        art_label="PODS",
        questions=(
            QuizQuestion(
                prompt="Which node component is responsible for keeping assigned Pods running?",
                options=(
                    "KUBELET",
                    "ETCD",
                    "SCHEDULER",
                    "INGRESS",
                ),
                correct_index=0,
                explanation="kubelet is the local node agent that starts, supervises, and reports on the Pods assigned to that node.",
            ),
            QuizQuestion(
                prompt="If a node becomes unhealthy, what usually happens to replacement workloads?",
                options=(
                    "THEY CAN BE RESCHEDULED ONTO A HEALTHIER NODE",
                    "THEY ARE PERMANENTLY DELETED FROM DESIRED STATE",
                    "THEY BYPASS THE CONTROL PLANE",
                    "THEY STOP USING SERVICE ROUTING",
                ),
                correct_index=0,
                explanation="The control plane keeps desired state intact and attempts to restore capacity elsewhere when conditions allow.",
            ),
        ),
    ),
    QuizTopic(
        key="networking",
        title="NETWORKING",
        description=TOPIC_DESCRIPTIONS["networking"],
        art_label="FLOW",
        questions=(
            QuizQuestion(
                prompt="What does kube-proxy primarily manage?",
                options=(
                    "LOCAL SERVICE ROUTING AND PACKET FORWARDING RULES",
                    "CONTAINER IMAGE VULNERABILITY SCANS",
                    "SCHEDULER LEADER ELECTION ONLY",
                    "PERSISTENT VOLUME FORMATTING",
                ),
                correct_index=0,
                explanation="kube-proxy programs the node so virtual service addresses can reach the right Pod backends.",
            ),
            QuizQuestion(
                prompt="Why is service abstraction useful in cluster networking?",
                options=(
                    "IT GIVES CLIENTS A STABLE ENDPOINT EVEN IF PODS CHANGE",
                    "IT DISABLES LOAD BALANCING",
                    "IT REMOVES THE NEED FOR PODS",
                    "IT PREVENTS NODES FROM TALKING TO THE CONTROL PLANE",
                ),
                correct_index=0,
                explanation="Services decouple clients from individual Pod lifecycles and maintain a stable access point.",
            ),
        ),
    ),
)
