async function fetchData() {
    try {
        // 캐시 방지를 위해 타임스탬프 추가
        const response = await fetch('diary_data.json?t=' + new Date().getTime());
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        renderDiary(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

function renderDiary(data) {
    const container = document.getElementById('diary-container');

    // 현재 표시된 데이터 개수와 새로운 데이터 개수가 같으면 업데이트 하지 않음 (간단한 비교)
    // 실제로는 ID 등을 비교하는 것이 좋지만, 여기서는 간단히 개수로 비교하거나
    // 전체를 다시 그리는 방식을 사용합니다. 애니메이션 효과를 위해 새로운 것만 추가하는 로직을 짤 수도 있습니다.
    // 여기서는 간단하게 기존 내용을 지우고 다시 그리는 방식보다는,
    // 내용을 비교해서 새로운 것만 추가하는 방식으로 구현해보겠습니다.

    // 하지만 요청사항이 "작성할때마다 배열 요소가 하나가 추가되잖아. 그때마다 사이트에 내용을 볼 수있는 div를 추가하도록 해줘" 이므로
    // 전체를 다시 렌더링하면 깜빡임이 있을 수 있으니, 
    // 현재 DOM 요소의 개수와 데이터의 개수를 비교합니다.

    const currentEntries = container.children.length;

    if (data.length > currentEntries) {
        // 새로운 데이터가 추가된 경우
        for (let i = currentEntries; i < data.length; i++) {
            const entry = data[i];
            const div = document.createElement('div');
            div.className = 'diary-entry';

            const dateDiv = document.createElement('div');
            dateDiv.className = 'diary-date';
            dateDiv.innerText = entry.date;

            const textDiv = document.createElement('div');
            textDiv.className = 'diary-text';
            textDiv.innerText = entry.text;

            div.appendChild(dateDiv);
            div.appendChild(textDiv);

            // 최신 글이 위로 오게 하려면 prepend, 아래로 쌓이게 하려면 append
            // 보통 일기장은 최신 글이 위로 오는게 좋지만, "배열 요소가 하나 추가될 때마다 div 추가"라는 말은
            // 순서대로 쌓이는 것을 의미할 수도 있습니다. 일단 배열 순서대로(오래된 것 -> 새 것) 아래에 추가하겠습니다.
            container.appendChild(div);
        }
    }
}

// 초기 로드
fetchData();

// 2초마다 데이터 확인 (폴링)
setInterval(fetchData, 2000);
