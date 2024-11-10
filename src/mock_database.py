from src.models import Machine, Kpi, Value, Alarm, Report, Configuration, KPIGroup
from datetime import datetime

mock_db = {
    "machines": [
        Machine(
            id="ast-yhccl1zjue2t",
            category="cutting_machines",
            name="Large Capacity Cutting Machine 1",
            kpi_list=[
                Kpi(
                    kpi_type="working_time",
                    machine_id="ast-yhccl1zjue2t",
                    data=[
                        Value(
                            machine_id="ast-yhccl1zjue2t",
                            sum=0.0,
                            avg=0.0,
                            min=0.0,
                            max=0.0,
                            var=0.0
                        ),
                    ],
                    config={}
                ),
                Kpi(
                    kpi_type="consumption",
                    machine_id="ast-yhccl1zjue2t",
                    data=[
                        Value(
                            machine_id="ast-yhccl1zjue2t",
                            sum=0.0661055170374786,
                            avg=0.0023213179492811795,
                            min=0.0,
                            max=0.0661055170374786,
                            var=0.0
                        ),
                    ],
                    config={}
                ),
                Kpi(
                    kpi_type="cycles",
                    machine_id="ast-yhccl1zjue2t",
                    data=[
                        Value(
                            machine_id="ast-yhccl1zjue2t",
                            sum=3373.0,
                            avg=1.0,
                            min=0.0,
                            max=28754.0,
                            var=0.0
                        ),
                    ],
                    config={}
                ),
            ]
        ),
        Machine(
            id="ast-yhccl1zjue2t",
            category="cutting_machines",
            name="Large Capacity Cutting Machine 2",
            kpi_list=[
                Kpi(
                    kpi_type="working_time",
                    machine_id="ast-yhccl1zjue2t",
                    data=[
                        Value(
                            machine_id="ast-yhccl1zjue2t",
                            sum=0.0,
                            avg=0.0,
                            min=0.0,
                            max=0.0,
                            var=0.0
                        ),
                    ],
                    config={}
                ),
                Kpi(
                    kpi_type="consumption",
                    machine_id="ast-yhccl1zjue2t",
                    data=[
                        Value(
                            machine_id="ast-yhccl1zjue2t",
                            sum=0.0661055170374786,
                            avg=0.0023213179492811795,
                            min=0.0,
                            max=0.0661055170374786,
                            var=0.0
                        ),
                    ],
                    config={}
                ),
                Kpi(
                    kpi_type="cycles",
                    machine_id="ast-yhccl1zjue2t",
                    data=[
                        Value(
                            machine_id="ast-yhccl1zjue2t",
                            sum=3373.0,
                            avg=1.0,
                            min=0.0,
                            max=28754.0,
                            var=0.0
                        ),
                    ],
                    config={}
                ),
            ]
        ),
        Machine(
            id="ast-yhccl1zjue2t",
            category="cutting_machines",
            name="Large Capacity Cutting Machine 3",
            kpi_list=[
                Kpi(
                    kpi_type="working_time",
                    machine_id="ast-yhccl1zjue2t",
                    data=[
                        Value(
                            machine_id="ast-yhccl1zjue2t",
                            sum=0.0,
                            avg=0.0,
                            min=0.0,
                            max=0.0,
                            var=0.0
                        ),
                    ],
                    config={}
                ),
                Kpi(
                    kpi_type="consumption",
                    machine_id="ast-yhccl1zjue2t",
                    data=[
                        Value(
                            machine_id="ast-yhccl1zjue2t",
                            sum=0.0661055170374786,
                            avg=0.0023213179492811795,
                            min=0.0,
                            max=0.0661055170374786,
                            var=0.0
                        ),
                    ],
                    config={}
                ),
                Kpi(
                    kpi_type="cycles",
                    machine_id="ast-yhccl1zjue2t",
                    data=[
                        Value(
                            machine_id="ast-yhccl1zjue2t",
                            sum=3373.0,
                            avg=1.0,
                            min=0.0,
                            max=28754.0,
                            var=0.0
                        )
                    ],
                    config={}
                )
            ]
        ),
    ],
    "alarms": [
        Alarm(
            text="High Power Consumption Alert",
            date=datetime.strptime("2024-03-01T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
            threshold=0.05,
            formula="consumption > threshold",
            machine_id="ast-yhccl1zjue2t"
        )
    ],
    "reports": [
        Report(
            id="rep-001",
            kpi_type="daily_summary",
            content="Daily machine performance report",
            date=datetime.strptime("2024-03-01T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
            uid="uid-001"
        )
    ],
    "configurations": [
        Configuration(
            children=[
                Kpi(
                    kpi_type="consumption",
                    machine_id="ast-yhccl1zjue2t",
                    data=[],
                    config={
                        "threshold": 0.05,
                        "alert_enabled": True
                    }
                )
            ],
            formula="consumption_working + consumption_idle",
            alarms=[]
        )
    ],
    "kpi_groups": [
        KPIGroup(
            name="Energy Metrics",
            kpi_list=[
                Kpi(
                    kpi_type="consumption",
                    machine_id="ast-yhccl1zjue2t",
                    data=[],
                    config={}
                ),
                Kpi(
                    kpi_type="power",
                    machine_id="ast-yhccl1zjue2t",
                    data=[],
                    config={}
                )
            ]
        )
    ]
}