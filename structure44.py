from collections import deque
from subway_graph2 import *

def dfs(graph, start_node):
    """dfs 함수"""
    stack = deque()  # 빈 스택 생성

    # 모든 노드를 처음 보는 노드로 초기화
    for station_node in graph.values():
        station_node.visited = 0

    
    start_node.visited = 1  # 시작 노드를 스택에 넣는다는 표시(옅은 회색)
    stack.append(start_node)    # 스택에 넣음

    while stack:    # 스택에 노드가 남아 있을 때까지
        current_station = stack.pop()   # 스택 가장 위(last) 데이터를 갖고온다
        current_station.visited = 2     # 현재 노드를 방문 표시
        for station in current_station.adjacent_stations:
            if station.visited == 0:    # 만약 처음 보는 노드라면
                station.visited = 1     # 스택에 넣는다는 표시(옅은 회색)
                stack.append(station)   # 스택에 넣음


stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
dfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)

